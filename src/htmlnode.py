class HTMLNode():
    def __init__(self, tag = None, value = None, children = None, props = None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props
    
    def to_html(self):
        raise NotImplementedError
    
    def props_to_html(self):
        string = ''
        if self.props is not None:
            for key in self.props:
                string += f' {key}="{self.props[key]}"'
        return string
    
    def __repr__(self):
        tag = False
        value = False
        children = False
        string = 'HTMLNode('
        if self.tag is not None:
            string += f'tag = {self.tag}'
            tag = True
        if self.value is not None:
            if tag:
                string += ', '
            string += f'value = {self.value}'
            value = True
        if self.children is not None:
            if value or tag:
                string += ', '
            string += f'children = {self.children}'
            children = True
        if self.props is not None:
            if children or value or tag:
                string += ', '
            string += f'props ={self.props_to_html()}'
        string += ')'
        return string

class LeafNode(HTMLNode):
    def __init__(self, tag, value, props = None):
        super().__init__(tag = tag, value = value, props = props)
    
    def to_html(self):
        if self.value is None:
            raise ValueError ("value is a required argument")
        if self.tag is None:
            return self.value
        if self.props is not None:
            if self.tag == "img":
                return f'<{self.tag}{self.props_to_html()}/>'
            elif self.tag == "a":
                return f'<{self.tag}{self.props_to_html()}>{self.value}</{self.tag}>'
        return f'<{self.tag}>{self.value}</{self.tag}>'

class ParentNode(HTMLNode):
    def __init__(self, tag, children, props = None):
        super().__init__(tag = tag, children = children, props = props)
    
    def to_html(self):
        if self.tag is None:
            raise ValueError ("tag is a required argument")
        if self.children is None:
            raise ValueError ("children is a required argument")
        string = f'<{self.tag}>'
        for child in self.children:
            string += child.to_html()
        string += f'</{self.tag}>'
        return string
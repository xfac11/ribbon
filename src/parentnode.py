from htmlnode import HTMLNode

class ParentNode(HTMLNode):
    def __init__(self, tag, children, props=None):
        super().__init__(tag, None, children, props)
    
    def to_html(self):
        if self.tag is None:
            raise ValueError("A parent node requires a tag")
        if self.children is None or len(self.children) == 0:
            raise ValueError("A parent node requires children")
        
        tag_str = f"<{self.tag}{self.props_to_html()}>"
        end_tag_str = f"</{self.tag}>"

        sum = ""
        for child in self.children:
            sum += child.to_html()
        
        return tag_str + sum + end_tag_str

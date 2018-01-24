class Comment(object):
    def __init__(self, text, date):
        self.text = text
        self.date = date

    # def __repr__(self):
    #     """Represent user as string."""
    #     return "text: {}, date: {}".format(
    #         self.text,
    #         self.date
    #     )


 # if __name__ == '__main__':
COMMENTS = [
    Comment("Coment 1", "2018-01-01"),
    Comment("Comment 2", "2018-01-02"),
    Comment("Comment 3", "2018-01-03"),
]

    def tr(self):
        """Return user as HTML table row."""
        tr = "<tr>"
        tr += "<td>{}</td>".format(self.text)
        tr += "<td>{}</td>".format(self.date)
        tr += "</tr>"
        return tr
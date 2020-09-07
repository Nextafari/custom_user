# mycharts.py
from reportlab.graphics.shapes import Drawing, String
from reportlab.graphics.charts.barcharts import VerticalBarChart


class MyBarChartDrawing(Drawing):
    def __init__(self, width=600, height=500, *args, **kw):
        Drawing.__init__(self, width, height, *args, **kw)
        self.add(VerticalBarChart(), name='chart')

        self.add(
            String(
                120, 480,
                'INVESTMENT/TRADE ANALYSIS (QUARTERLY HIGH & LOW)'
            ), name='title'
        )

        # set any shapes, fonts, colors you want here.  We'll just
        # set a title font and place the chart within the drawing
        self.chart.x = 20
        self.chart.y = 20
        self.chart.width = self.width - 20
        self.chart.height = self.height - 60

        self.title.fontName = 'Helvetica-Bold'
        self.title.fontSize = 12
        
        self.chart.data = [
            [100, 150, 200, 235, 100, 150, 200, 235]
        ]


if __name__ == '__main__':
    # use the standard 'save' method to save barchart.gif, barchart.pdf etc
    # for quick feedback while working.
    MyBarChartDrawing().save(
        formats=['gif', 'png', 'jpg', 'pdf'], outDir='.', fnRoot='barchart')

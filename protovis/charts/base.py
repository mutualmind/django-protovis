from protovis.widgets import ProtovisPanelWidget


class BaseChartWidget(ProtovisPanelWidget):
    """
    A base chart widget defining common elements that apply to most
    conventional charts.
    """
    
    def __init__(self, *args, **kwargs):
        super(BaseChartWidget, self).__init__(*args, **kwargs)
        self.sizing_and_scales()
        self.root_panel()
    
    def sizing_and_scales():
        raise NotImplementedError(
            'The sizing_and_scales method has not been implemented.'
        )

    def root_panel(self):
        self.width(self.pv_width) \
            .height(self.pv_height) \
            .bottom(20) \
            .left(20) \
            .right(10) \
            .top(5)

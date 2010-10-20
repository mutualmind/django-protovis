"""
This module was heavily inspired by the ToscaWidgets project.
"""
class JavaScriptSymbol:
    """
    Pythonic representation of a JavaScript code fragment.
    """
    def __init__(self, src):
        """
        Constructor.
        
        @param src: JavaScript source for this symbol
        @type src: string
        """
        self.src = src

class ProtovisObjects:
    """
    Pythonic representations of the protovis JavaScript object hierarchy:
    http://vis.stanford.edu/protovis/jsdoc/index.html
    """

    # represents an anchor on a given mark
    Anchor = JavaScriptSymbol(src='pv.Anchor')

    # represents an area mark: the solid area between two series
    # of connected line segments
    Area = JavaScriptSymbol(src='pv.Area')

    # represents a bar: an axis-aligned rectangle that can be stroked
    # and filled
    Bar = JavaScriptSymbol(src='pv.Bar')

    class Behavior(JavaScriptSymbol):
        # represents a reusable interaction; applies an interactive
        # behavior to a given mark
        src = 'pv.Behavior'

        # implements interactive dragging starting with mousedown events
        drag = JavaScriptSymbol(src='pv.Behavior.drag')

        # implements interactive panning starting with mousedown events
        pan = JavaScriptSymbol(src='pv.Behavior.pan')

        # implements interactive fuzzy pointing, identifying marks that
        # are in close proximity to the mouse cursor
        point = JavaScriptSymbol(src='pv.Behavior.point')

        # implements interactive resizing of a selection starting with
        # mousedown events
        resize = JavaScriptSymbol(src='pv.Behavior.resize')

        # implements interactive selecting starting with mousedown events
        select = JavaScriptSymbol(src='pv.Behavior.select')

        # implements interactive zooming using mousewheel events
        zoom = JavaScriptSymbol(src='pv.Behavior.zoom')

    class Color(JavaScriptSymbol):
        # represents an abstract (possibly translucent) color
        src = 'pv.Color'

        # represents a color in HSL space
        Hsl = JavaScriptSymbol(src='pv.Color.Hsl')

        # represents a color in RGB space
        Rgb = JavaScriptSymbol(src='pv.Color.Rgb')

    # a collection of standard color palettes for categorical encoding
    Colors = JavaScriptSymbol(src='pv.Colors')

    class Constraint(JavaScriptSymbol):
        # represents a constraint that acts on particles
        src = 'pv.Constraint'

        # constrains particles to within fixed rectangular bounds
        bound = JavaScriptSymbol(src='pv.Constraint.bound')

        # constraints circles to avoid overlap
        collision = JavaScriptSymbol(src='pv.Constraint.collision')

        # constraints particles to a fixed position
        position = JavaScriptSymbol(src='pv.Constraint.position')

    class Dom(JavaScriptSymbol):
        # represets a DOM operator for the specified map
        src = 'pv.Dom'

        # represents a Node in the W3C Document Object Model
        Node = JavaScriptSymbol(src='pv.Dom.Node')

    # represents a dot; a dot is simply a sized glyph centered at a
    # given point that can also be stroked and filled
    Dot = JavaScriptSymbol(src='pv.Dot')

    # represents a flatten operator for the specified array
    Flatten = JavaScriptSymbol(src='pv.Flatten')

    class Force(JavaScriptSymbol):
        # represents a force that acts on particles
        src = 'pv.Force'

        # an n-body force, as defined by Coulomb's law or Newton's
        # law of gravitation, inversely proportional to the square of
        # the distance between particles
        charge = JavaScriptSymbol(src='pv.Force.charge')

        # implements a drag force, simulating friction
        drag = JavaScriptSymbol(src='pv.Force.drag')

        # implements a spring force, per Hooke's law
        spring = JavaScriptSymbol(src='pv.Force.spring')

    class Format(JavaScriptSymbol):
        # represents an abstract text formatter and parser
        src = 'pv.Format'

        # the format string is in the same format expected by the
        # strftime function in C
        date = JavaScriptSymbol(src='pv.Format.date')

        # represents a number format, converting between a number
        # and a string
        number = JavaScriptSymbol(src='pv.Format.number')

        # represents a time format, converting between a number
        # representing a duration in milliseconds, and a string
        time = JavaScriptSymbol(src='pv.Format.time')

    class Geo(object):
        # represents a pair of geographic coordinates
        LatLng = JavaScriptSymbol(src='pv.Geo.LatLng')

        # represents a geographic projection
        Projection = JavaScriptSymbol(src='pv.Geo.Projection')
        
        # represents geographic projections
        projections = JavaScriptSymbol(src='pv.Geo.projections')

        # represents a geographic scale; a mapping between
        # latitude-longitude coordinates and screen pixel coordinates
        scale = JavaScriptSymbol(src='pv.Geo.scale')

        # tick functions for geographic scales
        scaleticks = JavaScriptSymbol(src='pv.Geo.scale#ticks')

    class histogram(JavaScriptSymbol):
        # represents a histogram operator
        src = 'pv.histogram'

        # represents a bin returned by the pv.histogram operator
        Bin = JavaScriptSymbol(src='pv.histogram.Bin')

    # represents an image, either a static resource or a dynamically-
    # generated pixel buffer
    Image = JavaScriptSymbol(src='pv.Image')

    # represents a text label, allowing textual annotation of
    # other marks or arbitrary text within the visualization
    Label = JavaScriptSymbol(src='pv.Label')

    class Layout(JavaScriptSymbol):
        # rRepresents an abstract layout, encapsulating a visualization
        # technique such as a streamgraph or treemap
        src = 'pv.Layout'

        # implements a layout for arc diagrams
        Arc = JavaScriptSymbol(src='pv.Layout.Arc')

        # implements a layout for bullets
        Bullet = JavaScriptSymbol(src='pv.Layout.Bullet')

        # implements a hierarchical layout using the cluster
        # (or dendrogram) algorithm
        Cluster = JavaScriptSymbol(src='pv.Layout.Cluster')

        # a variant of cluster layout that is space-filling
        Cluster.Fill = JavaScriptSymbol(src='pv.Layout.Cluster.Fill')

        # implements force-directed network layout as a node-link diagram
        Force = JavaScriptSymbol(src='pv.Layout.Force')

        # implements a grid layout with regularly-sized rows and columns
        Grid = JavaScriptSymbol(src='pv.Layout.Grid')

        # represents an abstract layout for hierarchy diagrams
        Hierarchy = JavaScriptSymbol(src='pv.Layout.Hierarchy')

        # implements a horizon layout, which is a variation of a
        # single-series area chart where the area is folded into multiple
        # bands
        Horizon = JavaScriptSymbol(src='pv.Layout.Horizon')

        # implements a hierarchical layout using the indent algorithm
        Indent = JavaScriptSymbol(src='pv.Layout.Indent')

        # implements a network visualization using a matrix view
        Matrix = JavaScriptSymbol(src='pv.Layout.Matrix')

        # represents an abstract layout for network diagrams
        Network = JavaScriptSymbol(src='pv.Layout.Network')

        # represents a link in a network layout
        Network.Link = JavaScriptSymbol(src='pv.Layout.Network.Link')

        # represents a node in a network layout
        Network.Node = JavaScriptSymbol(src='pv.Layout.Network.Node')

        # implements a hierarchical layout using circle-packing
        Pack = JavaScriptSymbol(src='pv.Layout.Pack')

        # implements a hierarchical layout using the partition
        # (or sunburst, icicle) algorithm
        Partition = JavaScriptSymbol(src='pv.Layout.Partition')

        # a variant of partition layout that is space-filling
        Partition.Fill = JavaScriptSymbol(src='pv.Layout.Partition.Fill')

        # implements a network visualization using a node-link diagram
        # where nodes are rolled up along two dimensions
        Rollup = JavaScriptSymbol(src='pv.Layout.Rollup')

        # implements a layout for stacked visualizations, ranging
        # from simple stacked bar charts to more elaborate "streamgraphs"
        # composed of stacked areas
        Stack = JavaScriptSymbol(src='pv.Layout.Stack')

        # implements a node-link tree diagram using the Reingold-Tilford
        # "tidy" tree layout algorithm
        Tree = JavaScriptSymbol(src='pv.Layout.Tree')

        # implements a space-filling rectangular layout, with the
        # hierarchy represented via containment
        Treemap = JavaScriptSymbol(src='pv.Layout.Treemap')

    # represents a series of connected line segments, or polyline,
    # that can be stroked with a configurable color and thickness
    Line = JavaScriptSymbol(src='pv.Line')

    # represents a data-driven graphical mark
    Mark = JavaScriptSymbol(src='pv.Mark')

    # represents a Nest operator for the specified array
    Nest = JavaScriptSymbol(src='pv.Nest')

    # represents a container mark
    Panel = JavaScriptSymbol(src='pv.Panel')

    # a weighted particle that can participate in a force simulation
    Particle = JavaScriptSymbol(src='pv.Particle')

    class Quadtree(JavaScriptSymbol):
        # represents a quadtree: a two-dimensional recursive spatial
        # subdivision
        src = 'pv.Quadtree'

        # a node in a quadtree
        Node = JavaScriptSymbol(src='pv.Quadtree.Node')

    # represents a horizontal or vertical rule
    Rule = JavaScriptSymbol(src='pv.Rule')

    class Scale(JavaScriptSymbol):
        # represents a scale; a function that performs a transformation
        # from data domain to visual range
        src = 'pv.Scale'

        # represents a linear scale; a function that
        # performs a linear transformation
        linear = JavaScriptSymbol(src='pv.Scale.linear')

        # represents a log scale
        log = JavaScriptSymbol(src='pv.Scale.log')

        # represents an ordinal scale
        ordinal = JavaScriptSymbol(src='pv.Scale.ordinal')

        # represents a quantile scale; a function that maps
        # from a value within a sortable domain to a quantized
        # numeric range
        quantile = JavaScriptSymbol(src='pv.Scale.quantile')

        # represents an abstract quantitative scale; a function
        # that performs a numeric transformation
        quantitative = JavaScriptSymbol(src='pv.Scale.quantitative')

        # represents a root scale; a function that
        # performs a power transformation
        root = JavaScriptSymbol(src='pv.Scale.root')

    # represents a particle simulation
    Simulation = JavaScriptSymbol(src='pv.Simulation')

    # represents a transformation matrix
    Transform = JavaScriptSymbol(src='pv.Transform')

    # represents a tree operator for the specified array
    Tree = JavaScriptSymbol(src='pv.Tree')

    # represents a two-dimensional vector; a 2-tuple (x, y)
    Vector = JavaScriptSymbol(src='pv.Vector')

    # protovis major and minor version numbers
    version = JavaScriptSymbol(src='pv.version')

    # represents a wedge, or pie slice
    Wedge = JavaScriptSymbol(src='pv.Wedge')

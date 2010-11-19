"""
This module was heavily inspired by the ToscaWidgets project.
"""
class JavaScriptFragment:
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

class js(JavaScriptFragment):
    """
    Convenience class for quickly writing JavaScript
    code fragments.
    """
    pass

class ProtovisObjects:
    """
    Pythonic representations of the protovis JavaScript object hierarchy:
    http://vis.stanford.edu/protovis/jsdoc/index.html
    """

    # represents an anchor on a given mark
    Anchor = JavaScriptFragment(src = 'pv.Anchor')

    # represents an area mark: the solid area between two series
    # of connected line segments
    Area = JavaScriptFragment(src = 'pv.Area')

    # represents a bar: an axis-aligned rectangle that can be stroked
    # and filled
    Bar = JavaScriptFragment(src = 'pv.Bar')

    class Behavior(JavaScriptFragment):
        # represents a reusable interaction; applies an interactive
        # behavior to a given mark
        src = 'pv.Behavior'

        # implements interactive dragging starting with mousedown events
        drag = JavaScriptFragment(src = 'pv.Behavior.drag')

        # implements interactive panning starting with mousedown events
        pan = JavaScriptFragment(src = 'pv.Behavior.pan')

        # implements interactive fuzzy pointing, identifying marks that
        # are in close proximity to the mouse cursor
        point = JavaScriptFragment(src = 'pv.Behavior.point')

        # implements interactive resizing of a selection starting with
        # mousedown events
        resize = JavaScriptFragment(src = 'pv.Behavior.resize')

        # implements interactive selecting starting with mousedown events
        select = JavaScriptFragment(src = 'pv.Behavior.select')

        # implements interactive zooming using mousewheel events
        zoom = JavaScriptFragment(src = 'pv.Behavior.zoom')

    class Color(JavaScriptFragment):
        # represents an abstract (possibly translucent) color
        src = 'pv.Color'

        # represents a color in HSL space
        Hsl = JavaScriptFragment(src = 'pv.Color.Hsl')

        # represents a color in RGB space
        Rgb = JavaScriptFragment(src = 'pv.Color.Rgb')

    # a collection of standard color palettes for categorical encoding
    Colors = JavaScriptFragment(src = 'pv.Colors')

    class Constraint(JavaScriptFragment):
        # represents a constraint that acts on particles
        src = 'pv.Constraint'

        # constrains particles to within fixed rectangular bounds
        bound = JavaScriptFragment(src = 'pv.Constraint.bound')

        # constraints circles to avoid overlap
        collision = JavaScriptFragment(src = 'pv.Constraint.collision')

        # constraints particles to a fixed position
        position = JavaScriptFragment(src = 'pv.Constraint.position')

    class Dom(JavaScriptFragment):
        # represets a DOM operator for the specified map
        src = 'pv.Dom'

        # represents a Node in the W3C Document Object Model
        Node = JavaScriptFragment(src = 'pv.Dom.Node')

    # represents a dot; a dot is simply a sized glyph centered at a
    # given point that can also be stroked and filled
    Dot = JavaScriptFragment(src = 'pv.Dot')

    # represents a flatten operator for the specified array
    Flatten = JavaScriptFragment(src = 'pv.Flatten')

    class Force(JavaScriptFragment):
        # represents a force that acts on particles
        src = 'pv.Force'

        # an n-body force, as defined by Coulomb's law or Newton's
        # law of gravitation, inversely proportional to the square of
        # the distance between particles
        charge = JavaScriptFragment(src = 'pv.Force.charge')

        # implements a drag force, simulating friction
        drag = JavaScriptFragment(src = 'pv.Force.drag')

        # implements a spring force, per Hooke's law
        spring = JavaScriptFragment(src = 'pv.Force.spring')

    class Format(JavaScriptFragment):
        # represents an abstract text formatter and parser
        src = 'pv.Format'

        # the format string is in the same format expected by the
        # strftime function in C
        date = JavaScriptFragment(src = 'pv.Format.date')

        # represents a number format, converting between a number
        # and a string
        number = JavaScriptFragment(src = 'pv.Format.number')

        # represents a time format, converting between a number
        # representing a duration in milliseconds, and a string
        time = JavaScriptFragment(src = 'pv.Format.time')

    class Geo(object):
        # represents a pair of geographic coordinates
        LatLng = JavaScriptFragment(src = 'pv.Geo.LatLng')

        # represents a geographic projection
        Projection = JavaScriptFragment(src = 'pv.Geo.Projection')

        # represents geographic projections
        projections = JavaScriptFragment(src = 'pv.Geo.projections')

        # represents a geographic scale; a mapping between
        # latitude-longitude coordinates and screen pixel coordinates
        scale = JavaScriptFragment(src = 'pv.Geo.scale')

        # tick functions for geographic scales
        scaleticks = JavaScriptFragment(src = 'pv.Geo.scale#ticks')

    class histogram(JavaScriptFragment):
        # represents a histogram operator
        src = 'pv.histogram'

        # represents a bin returned by the pv.histogram operator
        Bin = JavaScriptFragment(src = 'pv.histogram.Bin')

    # represents an image, either a static resource or a dynamically-
    # generated pixel buffer
    Image = JavaScriptFragment(src = 'pv.Image')

    # represents a text label, allowing textual annotation of
    # other marks or arbitrary text within the visualization
    Label = JavaScriptFragment(src = 'pv.Label')

    class Layout(JavaScriptFragment):
        # rRepresents an abstract layout, encapsulating a visualization
        # technique such as a streamgraph or treemap
        src = 'pv.Layout'

        # implements a layout for arc diagrams
        Arc = JavaScriptFragment(src = 'pv.Layout.Arc')

        # implements a layout for bullets
        Bullet = JavaScriptFragment(src = 'pv.Layout.Bullet')

        # implements a hierarchical layout using the cluster
        # (or dendrogram) algorithm
        Cluster = JavaScriptFragment(src = 'pv.Layout.Cluster')

        # a variant of cluster layout that is space-filling
        Cluster.Fill = JavaScriptFragment(src = 'pv.Layout.Cluster.Fill')

        # implements force-directed network layout as a node-link diagram
        Force = JavaScriptFragment(src = 'pv.Layout.Force')

        # implements a grid layout with regularly-sized rows and columns
        Grid = JavaScriptFragment(src = 'pv.Layout.Grid')

        # represents an abstract layout for hierarchy diagrams
        Hierarchy = JavaScriptFragment(src = 'pv.Layout.Hierarchy')

        # implements a horizon layout, which is a variation of a
        # single-series area chart where the area is folded into multiple
        # bands
        Horizon = JavaScriptFragment(src = 'pv.Layout.Horizon')

        # implements a hierarchical layout using the indent algorithm
        Indent = JavaScriptFragment(src = 'pv.Layout.Indent')

        # implements a network visualization using a matrix view
        Matrix = JavaScriptFragment(src = 'pv.Layout.Matrix')

        # represents an abstract layout for network diagrams
        Network = JavaScriptFragment(src = 'pv.Layout.Network')

        # represents a link in a network layout
        Network.Link = JavaScriptFragment(src = 'pv.Layout.Network.Link')

        # represents a node in a network layout
        Network.Node = JavaScriptFragment(src = 'pv.Layout.Network.Node')

        # implements a hierarchical layout using circle-packing
        Pack = JavaScriptFragment(src = 'pv.Layout.Pack')

        # implements a hierarchical layout using the partition
        # (or sunburst, icicle) algorithm
        Partition = JavaScriptFragment(src = 'pv.Layout.Partition')

        # a variant of partition layout that is space-filling
        Partition.Fill = JavaScriptFragment(src = 'pv.Layout.Partition.Fill')

        # implements a network visualization using a node-link diagram
        # where nodes are rolled up along two dimensions
        Rollup = JavaScriptFragment(src = 'pv.Layout.Rollup')

        # implements a layout for stacked visualizations, ranging
        # from simple stacked bar charts to more elaborate "streamgraphs"
        # composed of stacked areas
        Stack = JavaScriptFragment(src = 'pv.Layout.Stack')

        # implements a node-link tree diagram using the Reingold-Tilford
        # "tidy" tree layout algorithm
        Tree = JavaScriptFragment(src = 'pv.Layout.Tree')

        # implements a space-filling rectangular layout, with the
        # hierarchy represented via containment
        Treemap = JavaScriptFragment(src = 'pv.Layout.Treemap')

    # represents a series of connected line segments, or polyline,
    # that can be stroked with a configurable color and thickness
    Line = JavaScriptFragment(src = 'pv.Line')

    # represents a data-driven graphical mark
    Mark = JavaScriptFragment(src = 'pv.Mark')

    # represents a Nest operator for the specified array
    Nest = JavaScriptFragment(src = 'pv.Nest')

    # represents a container mark
    Panel = JavaScriptFragment(src = 'pv.Panel')

    # a weighted particle that can participate in a force simulation
    Particle = JavaScriptFragment(src = 'pv.Particle')

    class Quadtree(JavaScriptFragment):
        # represents a quadtree: a two-dimensional recursive spatial
        # subdivision
        src = 'pv.Quadtree'

        # a node in a quadtree
        Node = JavaScriptFragment(src = 'pv.Quadtree.Node')

    # represents a horizontal or vertical rule
    Rule = JavaScriptFragment(src = 'pv.Rule')

    class Scale(JavaScriptFragment):
        # represents a scale; a function that performs a transformation
        # from data domain to visual range
        src = 'pv.Scale'

        # represents a linear scale; a function that
        # performs a linear transformation
        linear = JavaScriptFragment(src = 'pv.Scale.linear')

        # represents a log scale
        log = JavaScriptFragment(src = 'pv.Scale.log')

        # represents an ordinal scale
        ordinal = JavaScriptFragment(src = 'pv.Scale.ordinal')

        # represents a quantile scale; a function that maps
        # from a value within a sortable domain to a quantized
        # numeric range
        quantile = JavaScriptFragment(src = 'pv.Scale.quantile')

        # represents an abstract quantitative scale; a function
        # that performs a numeric transformation
        quantitative = JavaScriptFragment(src = 'pv.Scale.quantitative')

        # represents a root scale; a function that
        # performs a power transformation
        root = JavaScriptFragment(src = 'pv.Scale.root')

    # represents a particle simulation
    Simulation = JavaScriptFragment(src = 'pv.Simulation')

    # represents a transformation matrix
    Transform = JavaScriptFragment(src = 'pv.Transform')

    # represents a tree operator for the specified array
    Tree = JavaScriptFragment(src = 'pv.Tree')

    # represents a two-dimensional vector; a 2-tuple (x, y)
    Vector = JavaScriptFragment(src = 'pv.Vector')

    # protovis major and minor version numbers
    version = JavaScriptFragment(src = 'pv.version')

    # represents a wedge, or pie slice
    Wedge = JavaScriptFragment(src = 'pv.Wedge')

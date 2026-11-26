---
{
  "module": "OAI/Computability/VPVNP/CompressorRecordsCursor.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/CompressorRecordsCursor.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/CompressorRecordsCursor.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Level-zero records of the compressor

Six parallel columns are indexed by a base or actual port number. At either
granularity the outgoing column stores an incoming port, and the incoming
column gives the unique outgoing port. Two additional columns give the base
arc's displacement and the actual arc's width. Every cell in these columns
has a direct address in the current level. To query a width at an incoming
port, follow that port's incoming entry into the width column.


### `IncidenceDirectory`

 A state-independent incidence directory for the native descriptor stages. 

### `IncidenceDirectory.baseOut`

 Base address of the column mapping each outgoing base port to its incoming mate. 

### `IncidenceDirectory.baseIn`

 Base address of the inverse column mapping each incoming base port to its outgoing mate. 

### `IncidenceDirectory.shift`

 Base address of the lane-displacement column indexed by outgoing base port. 

### `IncidenceDirectory.actualOut`

 Base address of the column mapping each outgoing actual port to its incoming mate. 

### `IncidenceDirectory.actualIn`

 Base address of the inverse column mapping each incoming actual port to its outgoing
  mate. 

### `IncidenceDirectory.width`

 Base address of the arc-width column indexed by outgoing actual port. 

### `basePort`

 Encode a base port as its base-site number times the degree plus its slot. 

### `actualPort`

 Encode an actual port by combining the base-site index, binary lane number, and slot in
that order. 

### `Represents`

 Complete base and actual incidence records of a state. 

### `Represents.incomingWidth`

 Read the actual source width at any incoming slot in two direct probes. 

### `greedyTables`

 Use these same base records in the greedy operand scans. 

### `BasePort`

 A level-zero cursor coordinate and base bit string together with one port slot. 

### `ActualPort`

 A level-zero base position refined by its lane bit string and a port slot. 

### `actualOrder`

 The loop counter enumerates all actual sources once. 

### `baseOrder`

 Number level-zero base ports consecutively in cursor-base order, with slots consecutive
inside each base position. 

### `publicWords`

 The eleven initializer operands giving the degree, cursor dimension, base and lane radices,
arc width, and six incidence column bases. 

### `directory`

 Lay out the six level-zero incidence columns at equally spaced addresses starting at the
supplied workspace location. 

### `typedRow`

 The level-zero record for an actual outgoing port, encoding its base source and target,
displacement, actual target, and width. 

### `visit_row`

 The actual emitted six values use the slot permutation of the typed state. 

### `column`

 Decode a row within a given column. The base arrays occupy prefixes of their
reserved regions. The words after each base prefix are immaterial. 

### `specification`

 Interpret an external address relative to the level's reserved region. 

### `initialize_cursor`

 From arbitrary memory, the fixed finite program initializes the graph directory of
the typed compressor. It visits every actual outgoing slot and accounts for six probes
plus one call. The full incoming columns follow from bijectivity of the slot matchings. 

### `initialization_cost`

 Linear cost in the Section 12 position count at fixed dyadic degree. 

### `eventually_initialize`

 At all sufficiently large input lengths the native initialization constructs the
complete Section 12 directory. The same threshold covers every partition of the virtual
address into a contiguous base block and lane block. 

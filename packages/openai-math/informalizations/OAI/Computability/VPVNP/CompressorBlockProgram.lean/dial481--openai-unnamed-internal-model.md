---
{
  "module": "OAI/Computability/VPVNP/CompressorBlockProgram.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/CompressorBlockProgram.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/CompressorBlockProgram.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# The online descriptor program for a fixed compression template

The initial four visits publish the cursor counts, construct its incidence
table and mark its role. One block contains the prescribed shrinking
substeps in increasing order and one degree refresh. Every phase computes
its operands from the live RAM. The script depends on the fixed compressor
template. The input size, iteration count and choices enter through RAM
and the branch tapes.

Table zero holds the greedy, rank, term and selected placement data of a
shrink, or the packed allocation of a refresh. Tables one through five
hold the AB intersections, surviving width and interval rows, sorted-slot
workspace, refresh preimages, and shrink resident tables, respectively.


### `refreshRate`

 Per-site scratch allowance for refresh segment columns, demands, term records, supply,
expander tables and output incidence. 

### `residentRate`

 The resident arrays contain twice the combined number of hidden and
map occurrences, plus one count for each new site in each directory. 

### `fieldCount`

 Reserved field count per table slot, covering the largest shrinking, refresh or resident
workspace with three extra fields. 

### `geometry`

 Only the scalar, table, slot and field dimensions are compiled into the
phase programs. The physical directory below uses the resulting catalog
arity and chronological row counts. 

### `arena`

 Expression reading the base address of one of the six tables at the given level. 

### `termPointers`

 Four visits publishing the term base, term stride, layout and absolute operand at header
offsets 36 through 39. 

### `shrink`

 Every selected graph level uses the old graph's published columns and
writes the next graph's canonical incidence columns. 

### `refreshPlacement`

 The singleton-child placement scan, using consecutive owner, count and child columns of one
word per site. 

### `refresh`

 The complete refresh visit sequence, including successor incidence copies, singleton
placement and the traversal metadata. 

### `initial`

 The initial header and cursor visits followed by publication of the cursor role at level
zero. 

### `block`

 One compression block, consisting of the shrinking steps in schedule order followed by the
refresh. 

### `script`

 The fixed script with its initial visits and its repeatable block of shrinking and refresh
visits. 

### `template`

 Finite instruction table for all inputs and all branch selections. 

### `native`

 Instantiate the block script as a RAM program at the supplied scheduler ports. 

### `allocationShape`

 The directory uses the program's actual arity. The capacity calculation
can reserve one complete block per state, and the physical run then takes
exactly the shorter chronological directory. 

### `layout`

 The physical descriptor layout for the given base, position capacity and block count, with
the directory sized to the actual visit count. 

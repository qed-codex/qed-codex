---
{
  "module": "OAI/Computability/VPVNP/PrimedCounterDispatchBounds.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/PrimedCounterDispatchBounds.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/PrimedCounterDispatchBounds.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Cursor bounds and the outer dispatch tests

At a legal item, the first five opcodes install the absolute cursor, its
successor and the public call count. Two unsigned comparisons distinguish the
input, site and histogram regions without wraparound.


### `ScheduleWords`

 The schedule words used by the actual jump and division opcodes. 

### `Item`

 A scheduled input cell, local parser operation or histogram comparison represented before
conversion to its absolute cursor. 

### `itemState`

 Persistent word supplied to the common program for this item. 

### `controlRegs`

 Registers after executing the first five literal instructions. 

### `laterRegs`

 Site and histogram regions also retain the absolute histogram start in register 17. 

### `compareRegs`

 Histogram comparison selects label `j` in operand register 7. 

### `input_pref`

 The input branch starts on its original cursor, with the native successor
and total installed outside the 48-register assembly operand space. 

### `row_pref`

 Every site cursor passes both outer phase tests, preserving the exact
absolute cursor and assembly boundary for the row division. 

### `compare_pref`

 The last region skips the site, subtracts the histogram start and passes
the resulting dense label index to the comparison code. 

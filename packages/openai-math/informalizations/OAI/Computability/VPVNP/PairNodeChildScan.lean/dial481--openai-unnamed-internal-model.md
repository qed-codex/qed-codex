---
{
  "module": "OAI/Computability/VPVNP/PairNodeChildScan.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/PairNodeChildScan.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/PairNodeChildScan.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Scanning a parent's actual descriptor children

The same guard, address calculation and slot routine run once per child,
independent of the row length. The pointer comes from external memory and
determines both the child's old incidence ordinal and its private buffer.


### `Sites`

 Program counters shared across iterations of a parent’s child scan, together with the
setup, width lookup and guess counters for each directed slot. 

### `Sites.guard`

 Locations of the three child-count instructions that either exit the scan or decrement
  the count and enter the address block. 

### `Sites.address`

 Locations of the seven instructions that fetch the child descriptor pointer, advance the
  source and calculate the first port and private argument address. 

### `Sites.slots`

 Instruction locations for processing each of the 2^a outgoing and 2^a incoming half-wire
  fields once the child address is known. 

### `LinkedWith`

 The entire body links back to the same guard after all slots of one child. 

### `Linked`

 The linkage interface for public slot-ordinal operands. 

### `Params`

 Register contents common to all children of the parent. 

### `mutableRegs`

 Only the slot temporaries, child address operands and loop counters may change. 

### `Frame`

 Register preservation across a child scan outside its eight mutable registers. In
particular the common incidence, row-layout and argument-arena parameters carry into the
next iteration. 

### `Ready`

 The source row, all old node pointers, and all destination fields fit in the word arena. 

### `ready_of_row`

 Specialize the bounds to the actual DFS row read by the parent. 

### `setupEvents`

 Trace before the first slot of a live child. Three guard ticks precede the external read at
src and the six ticks of address arithmetic. 

### `enter`

 Execute the guard and actual directory-pointer calculation for one live child. 

### `childEvents`

 One complete child, with its outgoing slots followed by its incoming slots. 

### `events`

 The chosen local instruction trace includes one empty-row exit. 

### `scanWith`

 Execute the full native row, preserving the continuation's entire choice
suffix and preparing precisely the logical ordered list of argument packets. 

### `reject_shortWith`

 An incomplete argument tape cannot return. This includes a short field
in a later child after all earlier guessed packets have been written. 

---
{
  "module": "OAI/Algorithms/SubexponentialSAT/SubexpMainReady.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/SubexpMainReady.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/SubexpMainReady.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Physical storage readiness after a leaf

The existing decoder and stack cleanup are followed by the actual finite
work-register reset program. These are storage facts, not an assumed semantic
layout contract. The main controller's final leaf cleanup is checked separately.


### `leafInput_ready`

 The parser writes protected control registers and persistent payload
ports, so it preserves the next layout call's ordinary storage readiness. 

### `execution`

 Register reset is an actual second procedure call, with its own halt and
the real final halt of sequential composition included in the bound. This
coarse bound counts all stored bits; `execution_selected` and
`execution_after_prefix` give bounds suitable for arbitrary pending streams. 

### `execution_selected`

 The pending stream and protected threshold bank do not contribute to
this bound: only selected workspace lengths are charged on entry. 

### `execution_after_prefix`

 Earlier phases are charged through their actual execution trace. Starting
with ready workspace makes the cleanup overhead independent of framed data. 

### `finished_stack_frame`

 The main leaf epilogue changes only the two reusable persistent stacks. 

### `finished_execution`

 The complete physical decoder and epilogue execute to a reusable storage
state. The epilogue's actual clearing cost is retained explicitly. 

### `finished_execution_after_prefix`

 The complete prefix, decoder, and leaf epilogue have a bound independent
of the unread pending stream and protected threshold contents. The current
leaf may grow during the prefix; that growth is charged to its actual steps. 

### `finished_callback_state`

 The real epilogue returns exactly the reader's next-iteration state,
with its original unread stream and an empty parser payload. 

### `next_leaf_ready`

 A subsequent parser callback and physical transfer start the next layout
with empty ordinary storage and the new leaf in forward order. 

---
{
  "module": "OAI/Computability/VPVNP/RAMTapeSiteEntryFrame.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/RAMTapeSiteEntryFrame.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/RAMTapeSiteEntryFrame.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Frame for installing the cut guard and preparing call inputs

The public operand table populates the native ISA public-word stacks. Its arithmetic scratch
may contain other data outside the call and cut banks. Only the parsed public fields and the
initially blank call workspace are relevant to the site-entry proof.


### `Frame`

 Physical input precondition. The public vector may already contain literal prefix operands. 

### `result_frame`

 The concrete public expression startup gives this frame directly. 

### `guardBank`

 Install the successor-guard output on its connected ports within the full processor bank. 

### `zeroBank`

 Guarded bank with a zero word installed in the native global-credit register. 

### `entryBank`

 Choice-entry bank with the unary choice budget exhausted and the selected bits on the
native choice stack. 

### `guarded_public_ne`

 The read-only public fields keep their original values. The incident field supplies the
suffix after the two successor messages. 

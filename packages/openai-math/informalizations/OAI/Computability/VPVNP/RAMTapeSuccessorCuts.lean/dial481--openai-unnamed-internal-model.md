---
{
  "module": "OAI/Computability/VPVNP/RAMTapeSuccessorCuts.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/RAMTapeSuccessorCuts.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/RAMTapeSuccessorCuts.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# From physical successor registers to the site's RAM cuts

The validator's word-level successor scan specifies the input and output cuts
and the two last records for the boundary check. On canonical incident fields
the physical stacks contain those same values, including the initial cut and
the missing output at the ends of the site chain.


### `sideCut`

 The word stacks at a missing send contain the zero, nonrunning cut. The
separate presence stack distinguishes it from a present halted target. 

### `sideRecord`

 Select the optional sent or received boundary record from a site's successor summary. 

### `CutRegisters`

 Register contents in terms of the word validator. Each cost occupies a
full word and has the stated natural value. Each record's encoded words
widen to the actual address, timestamp and ordinal in the transcript. 

### `Outputs.cutRegisters`

 Identify physical register outputs with any typed summary satisfying the
site successor specification. The lemma applies before and after the guard. 

### `guarded_cutRegisters`

 At the continuation of the guard, the exact stack representation agrees
with the word validator's successor scan on the same site and shared bits. 

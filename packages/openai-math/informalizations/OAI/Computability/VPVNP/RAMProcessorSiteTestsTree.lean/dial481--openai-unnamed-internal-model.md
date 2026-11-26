---
{
  "module": "OAI/Computability/VPVNP/RAMProcessorSiteTestsTree.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/RAMProcessorSiteTestsTree.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/RAMProcessorSiteTestsTree.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Finite decision trees on decoded site fields

Each test preserves the site data. The branch pop consumes its temporary
answer. A leaf returns the caller's exit tag on the verdict stack.


### `Atom`

 A site test that compares two word fields, inspects a status flag or checks whether the
choice stream is empty. 

### `Atom.eval`

 Boolean outcome of a primitive site check on the decoded words, flags and choices of a
snapshot. 

### `Atom.machine`

 Stack routine implementing an atomic site test and delivering its Boolean answer on the
left scratch stack. 

### `Atom.ticks`

 Exact stack-step count for an atomic test. A word comparison costs 20 times the width plus
10, a flag costs three, and testing choices costs two or three according to emptiness. 

### `Exit`

 Decision to reject execution, finish the current bucket or dispatch another charged call. 

### `Exit.bits`

 Verdict-stack encoding of the three exits. A leading false bit rejects, and a leading true
bit is followed by false for finish or true for dispatch. 

### `Tree`

 Finite decision tree with primitive site tests at branches and processor exits at leaves. 

### `Tree.eval`

 Follow the branch outcomes on a fixed decoded snapshot to obtain the processor exit at the
selected leaf. 

### `Tree.ticks`

 Exact stack-step count along the selected tree path, including each test, its branch pop
and the verdict bits pushed at the leaf. 

### `Tree.machine`

 Compile each branch to an atomic test and a pop that selects its successor. At a leaf the
routine pushes the encoded exit onto the verdict stack. 

### `Tree.run`

 A normally returning site test delivers its precise exit code. The
original choices, bounds, status bits and state words remain available. 

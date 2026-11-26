---
{
  "module": "OAI/Computability/VPVNP/VerifierMachineCook.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/VerifierMachineCook.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/VerifierMachineCook.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Boolean circuits for the gate-transcript verifier

The Cook–Levin compiler uses numbered wires and the AND/OR/NOT basis.
Translate its output to the AND/NOT basis of the VNP transcript construction,
with a bound of four gates per original gate and arbitrary input pinning.


### `Builder`

 The translated program and the current translation of each source wire. 

### `emit`

 Write one translated gate at the specified source-wire address. 

### `next`

 Temporary wires of the De Morgan expansion lie above every live source wire. 

### `initial`

 Each primary source input can be either an input variable or a Boolean constant. 

### `transcriptSize`

 Size of the compiled AND/NOT verifier circuit. 

### `toTranscriptWith`

 Compile an ordered Boolean circuit while substituting inputs or constants. 

### `toTranscriptWith_eval`

 Input pinning and gate translation agree with ordinary Boolean evaluation on every input. 

### `toTranscript`

 Translate with all primary inputs free. 

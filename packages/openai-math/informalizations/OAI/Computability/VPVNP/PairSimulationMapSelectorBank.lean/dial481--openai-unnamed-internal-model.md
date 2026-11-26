---
{
  "module": "OAI/Computability/VPVNP/PairSimulationMapSelectorBank.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/PairSimulationMapSelectorBank.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/PairSimulationMapSelectorBank.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Relocatable finite text of the complete motif selector phase

The directory scanner checks every incident selector suffix against the
anchor. It enters the fixed anchor decoder on agreement, and both parts
share a bad exit. The success address can be the first row-driver test.


### `Register`

 The selector phase's disjoint banks of eleven directory-scan registers and nine
anchor-decoder registers. 

### `Allocation`

 The first group holds port-scanner registers and the second holds
anchor-decoder registers. Public ports contain raw codes and ordinals. 

### `Allocation.register`

 Place the directory scanner's registers and the anchor decoder's registers at distinct
  positions in the enclosing machine. 

### `Allocation.port`

 Allocate distinct public ports to each selector's raw bit code and to its decoded
  ordinal. 

### `Location`

 Finite placement for all selector-stage opcodes and two continuation addresses. 

### `allocation`

 Standalone allocation that numbers all twenty selector registers and both public words of
each selector. 

### `scanReg`

 Physical register placement for the eleven registers of the incident port scanner. 

### `decoderReg`

 Physical register placement for the nine registers of the anchor selector decoder. 

### `codePort`

 Public port containing the raw selector code against which the extracted anchor bits are
compared. 

### `namePort`

 Public port containing the ordinal produced when the anchor decoder matches this selector's
code. 

### `lookup`

 Finite lookup flow that compares the extracted anchor field against the listed selector
codes and loads the matching ordinal into the decoder's output register. 

### `Address`

 Addresses of the selector phase, including the directory and agreement loops, the anchor
decoder and reader, the lookup rows for the given selector list, and both exits. 

### `program`

 The two components share the bad continuation. The successful decoder
leaves its ordinal array ready at the supplied success address. 

### `inBody`

 Test whether a selector-phase address designates an instruction body that an enclosing
program installs, with both continuations supplied by the caller. 

### `text`

 The finite text uses a normal or bad halt only in standalone placements.
A linked use installs the body and gives both exits to its enclosing program. 

### `linked`

 Matching the body text at its relocated addresses discharges the
instruction hypotheses of the port scan, bit comparison, field reader,
selector lookup and ordinal-writing loop simultaneously. 

### `words`

 Install the fixed public constants in a surrounding public-word bank. 

### `locations`

 Numbering this body and its exits gives a standalone finite template. 

### `template`

 Standalone finite selector template that enters the incident-port scan and accepts after
decoding the agreed anchor suffix or rejects a failed check. 

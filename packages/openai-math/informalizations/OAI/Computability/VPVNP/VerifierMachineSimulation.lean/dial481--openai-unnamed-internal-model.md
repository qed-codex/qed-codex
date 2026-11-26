---
{
  "module": "OAI/Computability/VPVNP/VerifierMachineSimulation.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/VerifierMachineSimulation.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/VerifierMachineSimulation.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Finite tape windows for the coefficient verifier

For a run of at most `r` steps, keep `2*r+1` cells of each tape centered at its
current head. A move shifts this array by one, reading a blank at the outside
edge. The cells with distance at most the remaining running time continue to
agree with the unbounded two-way tapes.


### `WindowCell`

 A cell of the finite tape window of radius `r`, numbered from the left edge. 

### `WindowTape`

 The symbol stored at each cell of a finite head-centered tape window. 

### `windowCenter`

 The cell scanned by the head in a radius-`r` window. 

### `shiftSource`

 The old cell which moves into a given position after a head motion. 

### `windowUpdate`

 Write the head cell, then move the head and shift the whole window. 

### `WindowConfig`

 A machine configuration restricted to the two tape windows used by the bounded verifier. 

### `WindowConfig.state`

 Current running or halting state in the window simulation. 

### `WindowConfig.firstTape`

 The head-centered window of the input tape. 

### `WindowConfig.secondTape`

 The head-centered window of the work tape. 

### `WindowRegister`

 State bits, followed by the symbol bits of the two finite tape windows. 

### `registerEncoding`

 Boolean tests for the current state at each candidate state index and for each candidate
symbol at every represented cell of either tape. 

### `windowBranches`

 Look up the literal transition row using the current state and the symbols at both window
centers. 

### `chosenInstruction`

 Select a branch using the path bit. A deterministic row accepts only the false choice bit. 

### `windowInstruction`

 Select the next instruction of a running configuration from the literal table and path bit. 

### `windowAdvance`

 Apply one instruction, updating the state and recentering both finite tape windows after
their head moves. 

### `windowStep`

 One deterministic step, including rejection of invalid choices and nonzero padding. 

### `windowOffset`

 Signed displacement of a window cell from the head. 

### `TapeAgrees`

 Agreement on all cells reachable in the remaining `t` transitions. 

### `WindowAgrees`

 The finite and unbounded configurations have the same state, and their two tapes agree at
every represented offset between minus t and t, inclusive. 

### `windowStep_agrees`

 One tick preserves agreement on the portion of the tape reachable by future ticks. 

### `windowRun`

 Run the machine on a finite window, consuming one bit per step. 

### `windowInitial`

 Load input bits on and to the right of the first tape head. 

### `windowRun_acceptsChoices`

 The bounded register machine computes the canonical witness predicate for the actual
two-way-tape program, including both halting states and all branch counts. 

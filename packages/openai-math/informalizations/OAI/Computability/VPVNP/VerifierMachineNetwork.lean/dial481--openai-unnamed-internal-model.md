---
{
  "module": "OAI/Computability/VPVNP/VerifierMachineNetwork.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/VerifierMachineNetwork.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/VerifierMachineNetwork.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Compiling finite arrays of local Boolean formulas

The coefficient verifier in §1.1 parses a table and then simulates one chosen transition
per clock tick. This interface indexes the existing Cook–Levin circuit compiler by named
finite types, so that table fields, tape cells, and input bits can be used directly as wire
indices. A layer preserves sharing between all previous gates.


### `Expr`

 Boolean expressions over the live wires of a verifier circuit. 

### `Frame`

 An array of live wire references in a circuit whose free inputs are indexed by `σ`. 

### `Frame.core`

 The gate fragment and its live wire references, with the input and output index types
  enumerated by finite ordinals. 

### `eval`

 Read the value of a chosen live wire under an assignment to the free inputs. 

### `size`

 Number of gates already emitted into the frame's circuit fragment. 

### `initial`

 The gate-free frame that selects its live wires directly from the inputs. 

### `step`

 Append a batch of Boolean expressions over the current live wires and expose their outputs
as the next frame. 

### `steps`

 Perform a sequence of indexed expression batches, retaining all previously emitted gates. 

### `select`

 Select live outputs without emitting any gates. 

### `withInput`

 Retain free inputs alongside a block's outputs for later layers. 

### `circuitSize`

 Designate a live wire as the output of the AND/NOT transcript circuit. 

### `circuit`

 Compile one selected output of the gate fragment as a single-output Boolean transcript
circuit. 

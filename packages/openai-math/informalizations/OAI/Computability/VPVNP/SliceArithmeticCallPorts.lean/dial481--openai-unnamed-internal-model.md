---
{
  "module": "OAI/Computability/VPVNP/SliceArithmeticCallPorts.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/SliceArithmeticCallPorts.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/SliceArithmeticCallPorts.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Ports of the reusable slice-field multiplication call

The external interface uses the same low-degree-first polynomial basis for
both operands. Each limb occupies a full arithmetic register. The internal
Horner machine has disjoint ports so its workspace can be reclaimed on return.


### `External`

 Caller ports for the prime, zero-word template, degree markers, reduction polynomial, query
scalar, and accumulator. 

### `Port`

 The stack interface for field multiplication, combining private Horner workspace with the
six caller ports. 

### `reg`

 Select arithmetic register `i` inside the multiplication call's Horner workspace. 

### `persistent`

 The multiplication workspace's persistent register-width template port. 

### `localStream`

 Embed a Horner coefficient-stream port into the multiplication call's private workspace. 

### `external`

 The caller's packed field parameters and operands, including one unary marker per extension
degree. 

### `clean`

 Clean entry and return boundaries. 

### `workspace`

 Combine a Horner register and stream bank with the external stacks of the multiplication
call. 

### `copies`

 Copy the persistent inputs, the three loop counts and the zero-register templates. 

### `occupied`

 Exactly the occupied internal ports after multiplication. 

### `reclaim`

 Replace the caller's accumulator with the finished Horner product and clear the occupied
private stacks. 

### `reclaim_runs`

 Copy the output to the caller, erase the old accumulator and reclaim
all local registers and streams. 

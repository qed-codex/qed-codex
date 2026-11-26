---
{
  "module": "OAI/Algorithms/SubexponentialSAT/Subexp/CollisionProgram.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/Subexp/CollisionProgram.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/Subexp/CollisionProgram.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# A fixed bit-program implementation of type collision

Each color is represented by an r-bit one-hot word.  All head and slot words
are serialized at a fixed width.  The existing fixed bitEqualityProgram
then compares two such encodings, including at the primitive-machine level.
The execution boundary has the two encoded types already on its two stacks;
seed lookup and the production of these encodings are separate operations.


### `typeWidth`

 The exact length of every type encoding. 

### `registerWord`

 Register zero is the head, and register i+1 is slot i. 

### `codeIndex`

 A computable position in the flattened register-position-color order. 

### `codeBit`

 One bit of the one-hot representation. 

### `encodeType`

 Uniform, fixed-width serialization of all type registers. 

### `collisionBool`

 The collision output specification.  Its implementation is the fixed
bitEqualityProgram, not evaluation of this proposition by a machine oracle. 

### `collisionBudget`

 Exact source-instruction upper bound, including the final empty-stack test. 

### `collision_trace`

 The existing ten-label program executes a correct type comparison.
All growing parameters appear only in the stack data. 

### `primitiveCollisionBudget`

 Primitive overhead is a constant of the one fixed equality program. 

### `outputCommand`

 Reuse the existing equality subroutine, then expose register 4 on the
output stack before the final halt.  No equality instructions are duplicated. 

### `collisionOutput_trace`

 The linked output routine needs just one push and one final halt beyond
the equality subroutine's already-counted return instruction. 

### `collisionOutput_primitive_runs`

 A real primitive-machine run whose terminal answer is the collision bit,
not merely an auxiliary register fact at a source boundary. 

### `assignedCollisionOutput_primitive_runs`

 The linked routine exposes the actual naturalPairTerm as its terminal bit. 

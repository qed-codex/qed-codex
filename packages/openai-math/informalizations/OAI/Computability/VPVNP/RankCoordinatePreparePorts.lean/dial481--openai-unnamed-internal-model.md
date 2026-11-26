---
{
  "module": "OAI/Computability/VPVNP/RankCoordinatePreparePorts.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/RankCoordinatePreparePorts.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/RankCoordinatePreparePorts.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

 # Shared advice and live ports of the two slice readers

The two machines read the same root templates, selector bank, and zero label
register. One advised scale is reserved for each operation. Dynamic register
zero and register one directly read the evaluator's two basis indices, and
the label converter directly reads its unary label. All three return intact.


### `Root`

 Paired-root workspace for the denominator and numerator determinant queries and their
finite-field quotient. The numerator’s entry workspace also carries the replacement-row and
target arguments. 

### `Parts`

 The combined root banks, dynamic ordinal registers, and unary-label workspace needed for
preparation. 

### `Advice`

 Immutable preparation advice, including the root images and the operation-dependent scale
words. 

### `Work`

 Writable preparation stacks, with an additional temporary port for copying. 

### `Ports`

 The reader bus carrying the immutable advice and the writable preparation banks separately. 

### `advice`

 Assemble the saved determinant roots, dynamic-register image, unary-label image, and the
two scale words as advice. 

### `work`

 Assemble the live preparation workspace with an initially empty copying stack. 

### `parts`

 Embed the collection of prepared stacks into the writable bank. 

### `root`

 Embed both determinant-root banks into the preparation workspace. 

### `dyn`

 Place the dynamic coordinate registers and ordinal-reader stacks in the preparation
workspace. 

### `unary`

 Place the unary-to-binary label converter in the preparation workspace. 

### `scratch`

 The temporary stack used when copying static roots and arguments. 

### `workPort`

 Access one writable preparation stack through the scalar reader's auxiliary port. 

### `scale`

 Read the operation-dependent scale word from the immutable advice bank. 

### `load`

 Copy the saved preparation data from advice into its writable counterpart using the
temporary stack. 

### `dynPort`

 Wire the dynamic selector's current and next registers to the reader's live ordinals and
mount its other ports in workspace. 

### `unaryPort`

 Wire the unary converter's source to the public label and its other ports to private
preparation stacks. 

### `dormant`

 Clear the current and next ordinal registers in the saved register image before they are
supplied by the caller. 

### `dynamic_bounded`

 Mount a selector run while leaving the two dormant template registers at
zero. The two active indices are the evaluator's persistent input words. 

### `labelCall`

 Frob keeps the zero mark. Label calls convert the live unary label to
its one-based binary mark and return the same label on its public port. 

### `labelTime`

 One step for the immediate return in Frobenius mode, or the unary-to-word conversion clock
for the one-based mark of a label operation. 

---
{
  "module": "OAI/Algorithms/SubexponentialSAT/SqrtLogSpace/SignatureTupleProgram.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/SqrtLogSpace/SignatureTupleProgram.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/SqrtLogSpace/SignatureTupleProgram.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Fixed-control interpreter for streaming signature tuples

The input-dependent depth is represented by an encoded stack of suspended
frames. `probe` tests one candidate against earlier assignments. A rejected
candidate advances at its current depth; only a fresh signature descends.
Thus this control table never traverses raw assignment tuples.

The subroutines are concrete finite commands, and all execution theorems use
their actual measured evaluations. Instantiating their frame, signature, and
counter invariants remains a separate native-program obligation.


### `Ports`

 Fixed Boolean control ports; all unbounded data live on bit stacks. 

### `Routines`

 Each field is a finite instruction table, rather than a semantic oracle.
`ascend` restores the parent's cursor and advances it once. `descend` saves
the current cursor and starts the child at its first Boolean assignment. 

### `Iteration`

 Concrete cases of one interpreter iteration. Their costs include every
Boolean branch, including the fresh-signature test's losing case. 

### `Traversal`

 Proof-level record of actual successive iterations; no trace is stored
by the executable program. The terminal guard test costs one step. 

### `program_trace`

 The same initialized controller yields an actual halted source trace. 

### `traversal_stack_bound`

 Every prefix of the actual fixed controller loop is covered. The body
bound must include suspended frames, all current words, and every scratch
stack; it must be proved uniformly before using this composition rule. 

### `pushFrameProgram`

 Consume the current generator payload and prepend its escaped reverse to
the suspended-frame stack. The verified parser recovers the original order. 

### `pushFrame_trace`

 Exact fixed-table suspension, including initialization and halt. 

### `popFrame_trace`

 Resume consumes one suspended frame and exactly restores its payload. 

### `suspendedFrames`

 Suspended generator records only; no completed tuples or key family. 

### `pushFrame_stack_bound`

 Local suspension uses linear time, so its every-prefix temporary space is
linear too. The persistent frame stack is included in the entry size. 

### `popFrame_stack_bound`

 Local resume includes every frame cell already present and the parser's
scratch/output cells at every source prefix. 

### `tupleStacks`

 The shared leaf ABI reserves twelve fixed physical ports. Their order is
frames, representatives, candidate, key, payload, scratch, depth, limit,
predecessor, predecessor key, and two scratch buffers. 

### `suspendCommand`

 Both calls preserve every caller stack outside the two designated ports. 

### `controllerPorts`

 The four controller flags are preserved by the smaller native routines.
Callbacks using the full register bank must use the shared caller-save wrapper. 

### `advanceCommand`

 One actual candidate advance. There is no construction of an assignment
list: both the cursor and remaining count are binary words. 

### `advanceTime_le`

 The per-candidate overhead is polynomial in word widths, although the
represented remaining count can be exponential. 

### `advanceState_available`

 Exhaustion is read from the full remaining word; no parity shortcut. 

### `advanceState_total`

 Cursor plus remaining fuel is unchanged by the actual candidate step. 

### `advanceState_widths`

 Binary words remain short even at the final overflow to the exact bound.
The exhausted word is never passed to the signature evaluator. 

### `advance_stack_bound`

 Every source prefix of the candidate advance includes the entire caller
frame. The added temporary storage is bounded by the two binary word widths. 

### `copyWord`

 Preserving copy uses one fixed empty scratch stack and two low registers. 

### `initialFuelPorts`

 The prepared head's unary size is copied as an all-zero initial assignment.
The length witness is consumed to initialize the binary remaining count. 

### `resetState_words`

 Empty heads are initialized with the sole empty assignment and fuel one. 

### `resetState_values`

 The reset creates the exact exponential fuel as a word of length `h+1`.
Its numeric value is used only in the proof, never as an executable loop list. 

### `reset_stack_bound`

 Reset's bound is uniform over all actual source prefixes, including the
persistent frame and representative stacks in the caller's entry storage. 

### `wordPorts`

 Two physical stack ports for a frame operation. 

### `saveCursorCommand`

 A suspended head retains exactly its cursor and remaining count. Matrix
rows and keys are reconstructed when the head resumes. 

### `recordRepresentativeCommand`

 Retain one emitted representative, with deepest head first on the physical
stack. The callback reconstructs its key from the exact retained assignment. 

### `descendLevelCommand`

 The remaining head count and physical color address are unary polynomial
words. They occupy two persistent ports, independent of the number of heads. 

### `clearWord`

 Clear a current-head word before reusing its physical stack. 

### `clearWords`

 The list specifies finitely many fixed physical ports in the control table;
it is never computed from or proportional to the assignment count. 

### `currentHeadPorts`

 These are the current generator's words. Suspended ancestors, emitted
representatives, remaining depth, and the physical head address are retained. 

### `dropRepresentativeCommand`

 Discard exactly one recorded representative after its subtree finishes. 

### `testParentCommand`

 Root detection uses the presence bit of the frame stack; a zero-bit or
empty payload frame is still present because it has an encoded delimiter. 

### `testAvailableCommand`

 Exact full-word test used before the candidate predicate is invoked. 

### `advanceState_assignment`

 Every nonterminal cursor is exactly the fixed-width word consumed by the
attained-signature predicate, not merely a short encoding of the same value. 

### `resetGeneratorCommand`

 A current-head reset initializes the predecessor cursor to the same
fixed-width zero word, preserving the freshly initialized candidate and fuel. 

### `pushWordState_register_frame`

 Generic frame operations preserve every controller flag. 

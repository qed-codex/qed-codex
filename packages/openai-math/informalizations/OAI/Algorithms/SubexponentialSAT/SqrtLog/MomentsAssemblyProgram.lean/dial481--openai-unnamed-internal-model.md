---
{
  "module": "OAI/Algorithms/SubexponentialSAT/SqrtLog/MomentsAssemblyProgram.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/SqrtLog/MomentsAssemblyProgram.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/SqrtLog/MomentsAssemblyProgram.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

 A raw framed-stream iterator with a mandatory native callback trace.
The invariant observes stacks, allowing the explicit peek instruction to use
scratch Boolean registers. All callback work is included in the bound. 

### `BodyContract`

 This is an explicit integration obligation for a real command. It cannot
be discharged by a semantic operation alone: each record requires an Eval. 

### `rawScan_eval`

 Every record is visited by the fixed while-loop and actual callback. 

 Physical nesting of the moment computation. Only the assignment producer
is a parameter: it is supplied as a fixed finite command, with a required Eval
contract in the execution theorem. Scaling, normalization, multiplication,
projection, record parsing, copies, and cleanup are concrete native programs.
The support and head masters are copied by paid loops for each actual use.


### `projectionScan`

 The support mask has already been parsed; scan the dictionary directly. 

### `assignmentStep`

 The producer consumes assignment174, returns scalar44 and dictionary41,
and preserves the current head sum42, head product40, and high contexts. 

### `finishSupport`

 Project the actual product, then add it into the running sparse answer. 

### `command`

 One fixed command for every number of buckets, supports, heads, and
assignments. None of those counts occurs in its finite control. 

### `coreState`

 Replacing the low arithmetic workspace preserves every ambient high tape. 

### `weightedAdd_eval`

 The wide head worker executes the concrete scale and normalize programs.
The current product on40 and all ambient high tapes are preserved. 

### `multiply_eval`

 Concrete multiplication of the current product by the completed head. 

### `projectionScan_eval`

 The support mask is already available from the outer loop. The native
projection scans every dictionary record and returns the retained records. 

### `project_eval`

 The actual relocated projection call, preserving all outer loop state. 

### `moveForward_eval`

 Forward movement is two actual reversing stack transfers. 

### `machine`

 The arithmetic workspace and arbitrary preserved ambient memory. 

### `afterTake_machine`

 Parsing a high record leaves every arithmetic tape untouched. 

### `startHead_eval`

 All three head fields are read by native frame loops; their sizes are paid. 

### `AssignmentContract`

 The only assembly callback. The assignment is actual runtime data, and
the contract demands a native Eval for its weight and factor-jet construction.
No head sums, head products, or projected moments are callback outputs. 

### `assignmentStep_eval`

 One assignment is parsed, produced by the paid worker, and immediately
accumulated by native sparse arithmetic. The source jet is then cleared. 

### `assignmentScan_eval`

 A complete paid traversal of one head's actual assignment records. 

### `move_core_eval`

 A low-workspace move is still implemented by the two paid stack scans. 

### `clear_high_eval`

 Clearing a high metadata tape preserves the entire arithmetic workspace. 

### `finishHead_eval`

 A completed head is multiplied into the running product by the native
sparse-ring program, and both metadata tapes are physically cleared. 

### `headStep_eval`

 A head record is decoded, its assignments are produced and added, and its
computed sum is multiplied into the current product. 

### `afterHead_eq`

 Head-local metadata and temporary streams have no residue after the head. 

### `headLoop_eval`

 Actual iteration over all head records; the incoming accumulator is a
physical sparse dictionary, and each head is computed from its assignments. 

### `project_machine_eval`

 Execute the exact-support projection with all unrelated arithmetic and
ambient tapes preserved. The encoded query was copied and reversed earlier. 

### `normalize_machine_eval`

 Native normalization adds projected records into the actual current
answer dictionary, using the ordinary runtime degree and modulus caches. 

### `finishSupport_eval`

 The support finish phase copies its mask, projects the computed head
product, adds into the actual accumulated answer, and restores all scratch. 

### `startBucket_eval`

 Decode a real bucket tuple, retain its head list as a master, and copy
its reusable support list by native list movement. 

### `supportStep_eval`

 One support is read from the actual support stream, every head is
computed, and the projected product is added to the actual answer tape. 

### `supportScan_eval`

 The actual support while-loop. The cost is the sum of all physical
support steps, including all nested assignment and head loops. 

### `bucketStep_eval`

 One actual bucket tuple: decode it, run the full support computation, and
clear only its metadata and head master after all contributions are added. 

### `command_eval`

 Complete physical bucket/support/head/assignment nesting. The sole
callback is the paid per-assignment producer; all moment arithmetic and
metadata movement are the concrete commands proved above. 

### `program_run`

 A finite compiled machine with the exact recursive runtime bound. The
producer is a fixed finite command, not a semantic oracle. 

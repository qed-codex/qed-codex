---
{
  "module": "OAI/Algorithms/SubexponentialSAT/SqrtLogSpace/SignatureTupleLoader.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/SqrtLogSpace/SignatureTupleLoader.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/SqrtLogSpace/SignatureTupleLoader.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

 Concrete head reloads for the attained-signature DFS.  The matrix comes
from the fixed native integer-entry machine, and each reload restores one
fixed retained-word bound before the next candidate scan. 

### `result`

 The physical result of that one concrete head loader. 

### `result_rescan_scratch`

 Every local rescan scratch word is blank after actual matrix staging. 

### `result_masters`

 The source words and caches retain their exact values across the loader. 

### `result_wordBound`

 The retained bound is restored exactly; the transient loader envelope is
never fed into the next boundary bound. 

### `load_run`

 The complete loader run is obtained from actual native inputs and paid
cache values. No successful matrix execution is an input to this theorem. 

### `result_reset_ready`

 The physically emitted full integer matrix initializes the actual
predecessor scanner at its zero candidate, including empty heads. 

### `shifted_rows_bounds`

 All raw incidence rows are present in the scanner, with polynomial
coefficient word lengths. No coordinate grid is materialized. 

### `integerMatrix`

 This is the literal signed owner-sum matrix, with every ambient head
coordinate retained in the actual ascending identifier order. 

### `shifted_key_kernel`

 Equality of the physically generated whole keys is exactly equality of
full integer signatures. Candidate indices are unchanged. 

### `retainedOutputBound_headroom`

 The fixed retained output envelope also pays the extra leading bit of
an exact power-of-two remaining-assignment word. 

### `load_reset_run`

 A fresh head is loaded and initialized by actual finite commands. The
same run establishes scanner readiness and retains the original bound F. 

### `retained_output_polynomial`

 The retained output cap itself is a fixed input polynomial, independent
of the caller's current storage bound and of the number of head reloads. 

### `runEnvelope`

 Both the time and every-prefix loader storage are bounded by one fixed
input polynomial. This envelope is transient and is never the next F. 

### `result_ancestor_storage`

 Reloading a head preserves the complete attained ancestor path. 

### `result_reset_scan_storage`

 A completed reload followed by the actual bounded counter initializer
establishes the next head's concrete scan boundary. 

### `descend_endpoint_bound`

 Internal descent retains only attained frames and the unary depth. Its
boundary bound depends on depth and word lengths, never on visited nodes. 

### `advance_candidate_ready`

 After a parent reload, the bounded advance preserves the actual scanner
input and establishes the next assignment without replaying an old rescan. 

### `resume_candidate_ready`

 Reloaded parent coefficients, restored cursor and an actual predecessor
copy give the next complete scanner input. 

### `initialControl_endpoint_bound`

 Initializing controller words restores the input cap before the first
matrix loader is invoked. 

### `fresh_descent_masters`

 The actual probe and attained descent preserve every loader source word
and native cache; only bounded cursor frames and the scanner latch change. 

### `result_cursor_words`

 Reloading changes the current matrix, while the restored bounded
candidate and remaining-assignment words retain their exact values. 

### `setup_native_run`

 The first positive-depth scan is reached by the actual fixed setup,
actual native head loader, and actual bounded counter initializer. 

### `ascend_native_run`

 Returning to a parent uses the actual native reload and advances its
restored cursor once. No earlier predecessor scan is repeated. 

### `descend_native_run`

 An attained internal child is reached by actual frame pushes, cleanup,
head loading and bounded counter setup, with the same retained cap F. 

### `result_address649`

 The native loader leaves its requested physical address on low649.
This is needed when a later pair restarts the same tuple traversal. 

### `exhausted_root_address649`

 Root exhaustion preserves the last root address, so the next pair can
initialize its traversal from low649 again. 

### `fresh_body_prefix_bound`

 The source compiler's conditional and sequence rules compose one
actual fresh probe and actual descent on a single bounded-prefix run. 

### `resume_loaded_address649`

 Restoring the predecessor and advancing a resumed cursor leave the
freshly loaded parent address on low649. 

### `scannerEnvelope`

 One fixed input polynomial bounds both the candidate scanner's retained
key and its transient space. The numerical candidate value is absent. 

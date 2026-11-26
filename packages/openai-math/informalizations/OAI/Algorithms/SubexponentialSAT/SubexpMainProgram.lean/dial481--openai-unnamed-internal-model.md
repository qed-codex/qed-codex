---
{
  "module": "OAI/Algorithms/SubexponentialSAT/SubexpMainProgram.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/SubexpMainProgram.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/SubexpMainProgram.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Fixed top-level SAT controller and caller storage convention

The controller hardwires the checked raw-input frontend, concrete framed-record
iteration, physical payload transfer, and output-bit handling. Remaining phases
are supplied as actual finite BitPrograms with explicit injective port maps.
Their semantic and resource contracts remain separate proof obligations.

The workspace has at least 16 Boolean registers and 128 stacks, plus fixed
extra space chosen with the clause width. Three further registers belong to the
record iterator. Thirty-two persistent stacks are disjoint from the workspace:
0..5 retain the raw-frontend ABI; 6 prime; 7 leaf stream; 8 reversed parser payload;
9 forward current leaf; 10 leaf answer; 11 final output; 12 modulus; 13 cell width;
14/15 field/basis data; 16 delta; 17 Q; 18 block size; 19 dimension; 20 threshold;
21 colors; 22 lifting precision. Later slots are explicit spare persistent data.


### `Procedure`

 A supplied phase is a fixed finite instruction table with explicit port
allocation. Its register map cannot touch any iterator-control bit. 

### `frontendProcedure`

 The real published parser/parameter frontend, allocated to persistent ports
0..5. No abstract preprocessing callback replaces it. 

### `prefix_execution`

 The first real phase accepts the existing canonical raw CNF syntax. 

### `Phases`

 The fields must be instantiated by real fixed finite programs. The record
contains no semantic function, answer, running-time annotation, or oracle. 

### `command`

 One concrete control graph: raw frontend, setup, actual sparsifier call,
framed leaf traversal with early success, and a physical output-bit push. 

### `transferLeaf_eval`

 A real transfer reverses the parser's reversed payload into the current
leaf stack and empties the parser payload. 

### `finishLeaf_eval`

 Pop the real decoded answer, clear reusable leaf storage with real loops,
and restore the record reader's control bits. 

### `LeafRun`

 Concrete executions of the four fixed leaf-processing programs. The
successive states and instruction counts are witnesses, not runtime inputs. 

### `leafInput`

 This is the physical state passed to a leaf callback by the framed parser. 

### `LeafContract`

 Every permitted leaf has measured executions of the actual four phase
programs. In addition to the computed answer, the contract explicitly restores
the pending record stream and parser payload. No Boolean test is executed by
this proposition: the program obtains its answer from its real decoder stack. 

### `BootRun`

 The fixed setup and sparsification procedures execute before leaf traversal.
The final state contains actual encoded leaf records produced by the latter. 

### `command_execution`

 All costs are real source instruction counts. The iterator pays for each
frame parse, leaf transfer, four phase calls, cleanup, branch, and final push.
The final state may retain workspace and persistent scalar data. 

### `compiled_execution`

 Source-code compilation has one final halt and no uncharged semantic step. 

### `primitive_execution`

 The actual primitive binary-tape machine returns the head bit while allowing
all other final work data to remain. Its overhead is fixed by the finite code. 

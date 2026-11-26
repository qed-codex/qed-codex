---
{
  "module": "OAI/Computability/VPVNP/LiveGroupModeInput.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/LiveGroupModeInput.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/LiveGroupModeInput.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Physical mode selection and the unit group count

The mode table reads slots two and three of processor zero and the widths
of the two cuts. Its unit tag, followed by the two padding scans, is
equivalent to the unit summand of the contraction. Its other tag selects
the evaluation summand of the first half or the tail, including at both
ends and when adjacent cuts have incompatible modes.


### `incidentWidth`

 The scheduled width of the cut incident to the given side of a group. 

### `firstHalfFlag`

 The Boolean test that a group lies in the initial half of the chain. 

### `physicalTag`

 The tag computed from the actual incident widths and processor-zero bits. 

### `physicalTag_evaluation`

 Evaluation is selected exactly when both actual interior modes are true.
The first-half flag distinguishes the pair and tail tags. 

### `unitPads`

 The two trailing padding intervals in unit mode. They may be empty. 

### `physicalTag_unit`

 Both complete cuts are zero precisely when the physical table chooses
the unit tag and the two padding intervals pass. 

### `PaddingSuccess`

 The native padding scan for the selected side succeeds on its full deterministic sequence
of calls. 

### `native_unit_count`

 Native acceptance of the two unit-padding scans, on the actual packed
headers and descriptor words, computes exactly the unit contribution. 

### `physical_mode_native`

 Public words 0 and 1 address the computed widths. The third scalar is
the first-half flag. From these words the fixed native table realizes
exactly the tag above on physical memory. 

### `physical_mode_rejects`

 When the two occupied modes disagree the native dispatcher rejects at
all fuel bounds and for every nondeterministic choice tape. 

### `physicalTag_pair`

 The pair tag occurs precisely on evaluation-mode groups of the first half. 

### `physicalTag_tail`

 The tail tag occurs precisely on evaluation-mode groups after the midpoint. 

### `routedCount`

 Dispatching by the actual mode-table result, with unit and evaluation
branches enforcing their respective checks. 

### `routed_specifiedGroupCount`

 The locally specified count on every raw cut assignment is the branch
chosen by the actual dispatcher. This includes malformed and mismatched modes. 

### `routed_pair_count`

 A first-half evaluation tag runs the pair whose raw exterior bits and
cumulative exponent fields occupy these physical cuts. 

### `routed_tail_count`

 The first tail group obtains its initial code from the middle exponents.
Each subsequent group parses the canonical code from its incoming cut. 

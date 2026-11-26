---
{
  "module": "OAI/Computability/VPVNP/RAMValidatorWork.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/RAMValidatorWork.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/RAMValidatorWork.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# The executable single-site RAM transcript validator

Each processor receives its own header word, a contiguous vector of incident
link bits, and a private binary branch path. It checks the two successor
fields, simulates the site's burst calls, and runs the local bitonic sorting
and memory boundary checks. The returned report sequence identifies the
successful path exactly, including coincident branches.


### `afterBucket`

 Apply the memory checks only to a successful bucket, preserving the work
already incurred when a malformed bit or unsuccessful call caused rejection. 

### `Machine.validateIncident`

 The interpreter's only inputs depending on the instance at other sites are
the bits delivered at this site's physical ports. 

### `Machine.validateIncident_iff`

 On an arbitrary shared assignment, one local binary string accepts with
the given reports precisely when the physical bit validator accepts them and
the string contains exactly the choices and read guesses of those reports. 

### `Machine.validateIncident_work`

 All received vectors and private bit streams meet the same bound,
including invalid control fields and rejected partial reads. 

### `Machine.validateIncident_clock`

 The paper's word-step cap for every path of the executable validator. 

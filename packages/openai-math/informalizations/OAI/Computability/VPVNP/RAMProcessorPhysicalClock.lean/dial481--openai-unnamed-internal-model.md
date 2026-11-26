---
{
  "module": "OAI/Computability/VPVNP/RAMProcessorPhysicalClock.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/RAMProcessorPhysicalClock.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/RAMProcessorPhysicalClock.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# The literal processor clock for the two RAM transcript applications

The estimate counts the site-entry and call loops, the closing checks, all
startup and sorting work, and the two-tape simulation of the named bit stacks.
The constants for a fixed template and its ports affect the threshold in the
input length. The clock exponent is uniform over the site and its choices.


### `perCallEstimate`

 Upper bound for starting a bucket call, resetting its registers and private
log, and executing its private and external instruction segments. 

### `eventually_stack_clock`

 Absorb all concrete stack stages into a single `n` power. The threshold is
independent of the register contents, site, bucket, and clock realization. 

### `eventually_physical_clock`

 Exact physical two-tape simulation overhead used by `input_count_labeled`. 

### `totalStackCutoff`

 Physical stack budget through the last incident-record check. The
postprocessor includes its sorting startup, all row exchanges, and its terminal
flag and boundary scans. 

### `le_totalStackCutoff`

 A graph realization whose individual call costs satisfy the physical
estimate is covered by the same total cutoff. 

### `ApplicationClock`

 The actual named-stack tape clock, including the closed memory checker,
at the paper's processor parameters. 

### `eventually_both_application_clocks`

 One length threshold covers the live and virtual processors, with their
respective private fuels `n^10000` and `n^10`. The two templates and their
numbers of ports and registers may differ. 

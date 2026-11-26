---
{
  "module": "OAI/Computability/VPVNP/RAMTapeBoundary.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/RAMTapeBoundary.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/RAMTapeBoundary.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Finite stack execution of the local predecessor and last-record checks

The sorted input is a contiguous sequence of five-word slots. Each interior
endpoint contributes its raw five-word last-record field. The machine tests
a clamped field for zero on missing edges. Width and slot count come from
unary stacks. Every field loop takes the same number of instructions on
arbitrary data, including after a failure has been latched.


### `work`

 Exact number of elementary stack steps, independent of the record bits. 

### `runs`

 The concrete finite control starts with just the two endpoint fields,
the sorted block, and two unary sizes. It implements all read, outgoing,
and clamping checks. It consumes the sorted block and both scratch stacks
finish empty. 

### `path_count`

 The deterministic pass contributes one accepting path exactly when
the scanned fields pass. The final instruction reads the latched status. 

### `path_count_checkAt_iff`

 On a site's actual parsed edge fields the terminal stack program has
one accepting path precisely when the local `checkAt` predicate holds and
the two missing endpoint fields, when present in the physical layout, are zero. 

---
{
  "module": "OAI/Computability/VPVNP/PairTraversalControllerBody.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/PairTraversalControllerBody.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/PairTraversalControllerBody.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Replaying the existing descriptor workers inside the traversal controller

The controller reads each parameter bank from live memory. When these words
match the completed level directory, each embedded body has the exact report
of its standalone reset-entry worker. In particular the controller adds no
write to those of the actual descriptor or role pass.


### `Pass`

 One traversal pass over a specified number of sites. A tag pass writes roles, a leaf pass
writes empty child headers, and a fiber pass translates child identifiers using its
capacity bound. 

### `Pass.count`

 Number of site-worker bursts scheduled for this pass. 

### `Pass.clock`

 Fuel per reference burst, fixed at 12 for tagging, 14 for leaf headers and `7 * cap + 25`
for fiber rows. 

### `Pass.spec`

 Instantiate the standalone tag, leaf or fiber worker with this pass's parameter words and
package its RAM program with its configuration type. 

### `Pass.At`

 A single reference burst started at site word `i` in memory `m` finishes within the pass
clock on an empty choice tape and returns `rep`. 

### `Pass.Run`

 Starting at site zero in `m`, the reference program produces the given reports across the
pass's scheduled bursts, each with its own empty choice tape. 

### `Pass.next`

 A successful standalone reference burst always returns the successor site. 

### `Pass.Bank`

 The three parameter banks are computed by the same fixed expression setup. 

### `Pass.body`

 Select the embedded role, leaf-header or fiber-row instruction flow that replays the
standalone worker inside the traversal controller. 

### `Pass.lift`

 Lift an actual standalone report, including its writes, into the common
word-width-independent controller. Every operand and output register outside
the seven worker temporaries is preserved. 

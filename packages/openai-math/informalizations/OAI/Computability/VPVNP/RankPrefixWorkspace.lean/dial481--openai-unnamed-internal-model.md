---
{
  "module": "OAI/Computability/VPVNP/RankPrefixWorkspace.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/RankPrefixWorkspace.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/RankPrefixWorkspace.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Reusing the rank workspace across prefix queries

Each call copies its fixed template into private work stacks. Designated
ports receive the live prefix-length word from register four. On return the
selected result word replaces register three, and every work port is cleared
before the next query.


### `Aux`

 Auxiliary ports of a prefix-rank call, with separate template and working stacks for each
callee port and one scratch stack for copies. 

### `Port`

 The five prefix-search word registers together with the private workspace used for calls to
the rank machine. 

### `auxBank`

 Initialize the template and working stacks from two banks, leaving the copy scratch empty. 

### `bank`

 The complete stack bank for a prefix-rank call, with the supplied template, working stacks,
and five word registers. 

### `workPort`

 The caller stack holding the working copy of a particular port of the rank machine. 

### `prepared`

 Contents of a working stack before a rank call. Dynamic ports receive the prefix word in
register four, and the others receive their template stacks. 

### `copyIn`

 Populate every working port from the prefix word or its template stack according to the
dynamic-port predicate. 

### `copyClock`

 Step bound for copying one input stack of length at most M into each of the rank workspace
ports. 

### `returnClock`

 Step bound for clearing register three, copying the w-bit rank into it, and erasing all
working stacks. 

### `copyIn_bounded`

 Copy the live prefix length and template into all callee ports without
consuming either source. Every caller register survives the preparation. 

### `callRank`

 Any bounded callee run changes only its private work stacks. 

### `returnRank`

 Replace register three by the word from the callee’s result port and clear the working
stacks for the next prefix query. 

### `returnRank_bounded`

 Return a complete rank word, reclaim every private port, and restore all
prefix-machine registers other than the result register. 

### `rankCall`

 Prepare, invoke, and reclaim one rank workspace while retaining the
immutable template for any later prefix. 

### `callSpace`

 Stack-height allowance for staging and returning a prefix-rank call when the incoming bank
has stack heights at most M. 

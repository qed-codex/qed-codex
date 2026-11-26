---
{
  "module": "OAI/Algorithms/SubexponentialSAT/SqrtLog/HashCircuitProgramInterpreter.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/SqrtLog/HashCircuitProgramInterpreter.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/SqrtLog/HashCircuitProgramInterpreter.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

 Component: HashCircuitProgramLiteralCallback. All public namespaces and APIs are retained. 

 Literal callback with actual lookup, polarity, sparse product, and return.
The represented minus-one and one values are explicit cached inputs. All work
is performed by the fixed native commands wired into the row interpreter. 

 Component: HashCircuitProgramClause. All public namespaces and APIs are retained. 

 Typed clause traversal using the fixed native literal callback. Input is
still the original unary literal encoding; the type is used only to specify
which dictionary entry the native decoder and lookup retrieve. 

### `command_eval`

 The fixed clause loop visits every original literal. Its cost recurrence
includes every physical frame read, arithmetic callback and loop branch. 

 Component: HashCircuitProgramRow. All public namespaces and APIs are retained. 

 The actual nested hash-row interpreter. The only inputs below are serialized
literal clauses, flat represented scalars, the selected incidence dictionary,
and the ring/cache words used by the native services. 

### `loop_eval`

 Every weighted clause is read from the supplied row and executed once. 

 Component: HashCircuitProgramRun. All public namespaces and APIs are retained. 

 Compiled fixed-program trace for one serialized sparse hash row. The
initial accumulator is physically cleared, and the final halt is charged. 

### `result_stack`

 The final physical output port is exactly the computed sparse dictionary. 

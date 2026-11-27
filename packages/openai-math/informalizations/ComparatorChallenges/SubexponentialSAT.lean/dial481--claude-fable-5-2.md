---
{
  "module": "ComparatorChallenges/SubexponentialSAT.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Claude Fable 5.2",
  "kind": "ai",
  "origin": "generated",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "license": "CC-BY-4.0"
}
---

# Informalization of ComparatorChallenges/SubexponentialSAT.lean: one statement about counting satisfying assignments on a Turing machine

**This file states one theorem and does not prove it. For every clause width $k \ge 2$ there is a deterministic multitape Turing machine with the following property. Given a CNF formula on $n$ variables whose clauses have at most $k$ literals, it writes the exact number of satisfying assignments and whether there is one. It halts within $C (b+1)^d \, 2^{A n (\ln\ln(n+16))^2 / \sqrt{\ln(n+16)}}$ steps, where $b$ is the length of the input in bits, and at no time has it visited more than $S (b+1)^e$ tape cells. The machine and the constants may depend on $k$.** The theorem ends in `sorry`, as the statement of a challenge does. A Comparator configuration names another module as its solution. The statement does not mention the Exponential Time Hypothesis. The repository's note on this formalization has the title "The Exponential Time Hypothesis is False".

AI drafted this autoinformalization from the original source. It is open for mathematical review.

## What kind of file this is

The file has 220 lines. It imports only Mathlib. [Line 1](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/ComparatorChallenges/SubexponentialSAT.lean#L1) It defines formulas, the input word, a machine model and the two bounds, and then states one theorem, `exact_count_and_sat`, with the body `sorry`. [Lines 191–218](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/ComparatorChallenges/SubexponentialSAT.lean#L191-L218)

A Comparator configuration beside the file names it as the challenge module and `OAI.Algorithms.SubexponentialSAT.Main` as the solution module. It lists this one theorem and permits the axioms `propext`, `Quot.sound` and `Classical.choice`. It sets `enable_nanoda` to `false`. [SubexponentialSAT.json, lines 1–14](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/ComparatorChallenges/SubexponentialSAT.json#L1-L14) In Comparator, setting that switch to `true` adds a check with a second kernel, nanoda, to the check with Lean's own kernel. [Comparator README, lines 12–13](https://github.com/leanprover/comparator/blob/865edc14486c3388e9225daa971da8e157488c3e/README.md?plain=1#L12-L13) [Comparator README, lines 86–87](https://github.com/leanprover/comparator/blob/865edc14486c3388e9225daa971da8e157488c3e/README.md?plain=1#L86-L87) I have not built the project and have not run Comparator.

The repository README says that the manuscripts and proof artifacts were produced by an unnamed internal OpenAI model, and that the collection includes results at different stages of verification. [README, line 3](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/README.md?plain=1#L3) [README, line 7](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/README.md?plain=1#L7)

## Formulas

A literal is a variable with a sign. A clause is a finite set of literals and a formula is a finite set of clauses. Being sets, they have no order and no repetition. An assignment gives each variable a truth value. [Lines 17–25](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/ComparatorChallenges/SubexponentialSAT.lean#L17-L25) A literal is true under an assignment if the value of its variable equals its sign. A clause is true if one of its literals is, and a formula is true if all of its clauses are. So the empty clause is never true and the empty formula is always true. [Lines 29–36](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/ComparatorChallenges/SubexponentialSAT.lean#L29-L36) A formula has width at most $k$ if every clause has at most $k$ literals. [Line 38](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/ComparatorChallenges/SubexponentialSAT.lean#L38) When the type of variables is finite, `count F` is the number of assignments of all the variables under which $F$ is true. [Lines 42–47](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/ComparatorChallenges/SubexponentialSAT.lean#L42-L47)

## The input word

The variables are $0, \dots, n-1$. A literal gets the number $2i$ for the negated variable $i$ and $2i + 1$ for the variable itself. A clause becomes the list of its numbers in increasing order, and a formula the list of these lists in increasing order. [Lines 64–71](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/ComparatorChallenges/SubexponentialSAT.lean#L64-L71) The order on lists is the relation `≤` of Lean's library, which compares two lists as a dictionary compares two words. I take that from the library and not from this file.

Numbers are written in unary: the number $m$ is $1^m 0$. [Line 55](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/ComparatorChallenges/SubexponentialSAT.lean#L55) A list is written item by item. Each item starts with a $1$, then comes the code of the item with a $1$ before each of its bits and a $0$ after the last one. The list ends with a $0$. [Lines 57–62](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/ComparatorChallenges/SubexponentialSAT.lean#L57-L62) The input word is $n$ in unary followed by the formula as a list of lists of numbers. Its length is `formulaBitLength F`, called $b$ in this note. [Lines 73–79](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/ComparatorChallenges/SubexponentialSAT.lean#L73-L79)

## The machine

A `PrimitiveMachine` has finitely many tapes and finitely many states. Each state names the one tape that it scans. The transition takes the state and the scanned symbol, which is a bit or a blank. It either halts with a Boolean answer or gives a next state and one action on the scanned tape: a move of the head by one cell, or a write. [Lines 92–119](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/ComparatorChallenges/SubexponentialSAT.lean#L92-L119) So a step is one move or one write on one tape, or it is the last step, which enters the halted state and changes no tape. At the start the input is on the input tape and the other tapes are empty. [Lines 121–124](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/ComparatorChallenges/SubexponentialSAT.lean#L121-L124) `Trace step t a c` says that $c$ is reached from $a$ in exactly $t$ steps. [Lines 87–90](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/ComparatorChallenges/SubexponentialSAT.lean#L87-L90)

## The two bounds

**Time.** Put $\sigma(n) = n (\ln\ln(n+16))^2 / \sqrt{\ln(n+16)}$. The time bound is $C (b+1)^d \, 2^{A \sigma(n)}$. [Lines 132–139](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/ComparatorChallenges/SubexponentialSAT.lean#L132-L139) The logarithms are natural logarithms.

**Space.** For each tape the file keeps the position of the head and a lower and an upper mark. All of them start at $0$, except that the upper mark of the input tape starts at the last cell of the input. Each move of a head updates its position and its two marks. The visited space is the sum over the tapes of upper $-$ lower $+\,1$. So the cells of the input count from the start, and every other tape counts at least one cell. [Lines 149–189](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/ComparatorChallenges/SubexponentialSAT.lean#L149-L189)

## The statement

For every $k \ge 2$ there are a machine, two of its tapes called the count tape and the answer tape, real numbers $C, A, S > 0$ and natural numbers $d, e > 0$ such that the following holds for every $n$ and every formula $F$ of width at most $k$ on the variables $0, \dots, n-1$. There are a number of steps $t$ and a final configuration with these properties. [Lines 194–217](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/ComparatorChallenges/SubexponentialSAT.lean#L194-L217)

1. The final configuration is reached from the start on the input word of $F$ in exactly $t$ steps.
2. The count tape holds exactly the word for `count F` in binary, lowest bit first, with the head on its first bit and blanks everywhere else. The number $0$ is written as the single bit $0$. [Line 147](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/ComparatorChallenges/SubexponentialSAT.lean#L147)
3. The answer tape holds exactly one bit, under the head, which is $1$ exactly when `count F` is positive.
4. The machine has halted with that same bit as its answer.
5. $t \le C (b+1)^d \, 2^{A \sigma(n)}$.
6. After every number of steps up to $t$ the visited space is at most $S (b+1)^e$.

The statement also records two facts about the binary word alone: it decodes to `count F` under the file's decoder `toNat`, [Lines 5–9](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/ComparatorChallenges/SubexponentialSAT.lean#L5-L9) and it has at most $n + 1$ bits. [Lines 208–209](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/ComparatorChallenges/SubexponentialSAT.lean#L208-L209)

## Points that need care

- **One machine for each $k$.** The comment on the theorem begins "One fixed primitive machine". [Lines 191–193](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/ComparatorChallenges/SubexponentialSAT.lean#L191-L193) In the statement the machine is chosen after $k$, so it is fixed for each $k$ and may differ from one $k$ to the next. The constants may depend on $k$ too.
- **All $n$ variables count.** The count is over all $2^n$ assignments, whether or not every variable occurs in $F$.
- **Only the input words of formulas.** The statement speaks about the input word of a formula of width at most $k$. It says nothing about what the machine does on any other word.
- **The factor in $b$.** The bound has a polynomial factor in the length of the input, and numbers are written in unary. For fixed $k$ this does no harm to the exponent: a formula is a set of clauses, so it has at most $(2n+1)^k$ of them, and $b$ is bounded by a polynomial in $n$. Since $\sigma(n)/n$ tends to $0$, the bound is then $2^{o(n)}$.
- **The Exponential Time Hypothesis.** The file does not define it and does not mention it. The repository's note on this formalization has the title "The Exponential Time Hypothesis is False" and names this file as the Comparator statement of the result. [lean/docs/378.md, lines 1–17](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/docs/378.md?plain=1#L1-L17) The list of contents has the entry "Disproof of the Exponential Time Hypothesis" with a link to that note. [CONTENTS.md, lines 9154–9163](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/CONTENTS.md?plain=1#L9154-L9163) As usually stated, the hypothesis says that for some $\delta > 0$ no algorithm decides 3-SAT on $n$ variables in time $2^{\delta n}$. By the point above, the statement here at $k = 3$ gives a deterministic machine that decides it in $2^{o(n)}$ steps, which contradicts the hypothesis. This inference is mine. It is not written in this file, and the `sorry` here proves none of it.

## What the statement leaves out

- **The proof.** This file has none.
- **The constants.** They are said to exist. No value is given.

## What I read

I read this file in full, its Comparator configuration, the entry for this result in `CONTENTS.md`, the note `lean/docs/378.md` and the first lines of the repository README, at the linked revision. I read the lines of the Comparator README that describe the second kernel. I did not read the manuscript. I did not read the proof, and I did not build the project.

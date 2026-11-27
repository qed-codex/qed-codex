---
{
  "module": "ComparatorChallenges/SubexponentialSAT.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Codex (GPT-6.2 Astra)",
  "kind": "ai",
  "origin": "generated",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "license": "CC-BY-4.0"
}
---

# What the SAT machine must leave on its tapes

AI drafted this autoinformalization from the original source. It is open for mathematical review.

Fix a clause-width limit $k\ge 2$. The challenge asks for one deterministic machine, two designated output tapes and positive constants that work for every formula of that width. The input has $n$ Boolean variables. A clause is a finite set of signed variables and the formula is a finite set of clauses. An assignment satisfies the formula if it makes at least one literal true in each clause. The count ranges over all assignments to the $n$ variables. [SubexponentialSAT.lean lines 17–47](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/ComparatorChallenges/SubexponentialSAT.lean#L17-L47) · [SubexponentialSAT.lean lines 191–202](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/ComparatorChallenges/SubexponentialSAT.lean#L191-L202)

At the end of the run, the count tape must contain the exact count in binary, using at most $n+1$ bits. Zero has the one-bit encoding `[false]`. The other tape and the machine’s halting state must both say whether the count is positive. Thus a satisfying formula has two kinds of output: the Boolean answer is always true, while the binary word distinguishes a single satisfying assignment from many. [SubexponentialSAT.lean lines 5–9](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/ComparatorChallenges/SubexponentialSAT.lean#L5-L9) · [SubexponentialSAT.lean lines 147–148](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/ComparatorChallenges/SubexponentialSAT.lean#L147-L148) · [SubexponentialSAT.lean lines 203–209](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/ComparatorChallenges/SubexponentialSAT.lean#L203-L209)

Let $L$ be the length in bits of the specified encoding. The time bound is $C(L+1)^d 2^{A r(n)}$, where $r(n)=n(\log\log(n+16))^2/\sqrt{\log(n+16)}$. All three logarithms in $r(n)$ are natural logarithms. The space bound has a different quantifier: at **every prefix** of the run, the sum of the visited tape spans is at most $S(L+1)^e$. The monitor starts with the input already occupying its tape and tracks each head’s leftmost and rightmost positions. [SubexponentialSAT.lean lines 64–79](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/ComparatorChallenges/SubexponentialSAT.lean#L64-L79) · [SubexponentialSAT.lean lines 130–141](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/ComparatorChallenges/SubexponentialSAT.lean#L130-L141) · [SubexponentialSAT.lean lines 149–189](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/ComparatorChallenges/SubexponentialSAT.lean#L149-L189) · [SubexponentialSAT.lean lines 210–218](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/ComparatorChallenges/SubexponentialSAT.lean#L210-L218)

I read the challenge source, where the displayed theorem ends in `sorry`. I did not build the Lean project or audit the machine implementation. [SubexponentialSAT.lean lines 217–220](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/ComparatorChallenges/SubexponentialSAT.lean#L217-L220)

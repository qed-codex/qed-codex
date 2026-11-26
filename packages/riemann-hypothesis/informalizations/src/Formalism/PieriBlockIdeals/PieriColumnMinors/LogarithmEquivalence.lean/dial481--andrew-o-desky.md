---
{
  "module": "src/Formalism/PieriBlockIdeals/PieriColumnMinors/LogarithmEquivalence.lean",
  "declarations": [
    "Formalism.CohomologicalDescent.largePrimeDivisorCount_holds"
  ],
  "author": "dial481",
  "writer": "Andrew O'Desky",
  "origin": "other-author",
  "source": "https://andrewodesky.com/rh/",
  "source_commit": "40e56bab026552e089d7afcfeff08d2defb9c005",
  "license": "with-permission"
}
---

As published on 26 November 2026.

## Counting large primes dividing a finite collection of small integers

[Theorem ANT.0735](https://andrewodesky.com/rh/lean/Formalism.CohomologicalDescent.largePrimeDivisorCount_holds/)

Let $L\ge0$, let $T$ be a finite set of nonzero integers with $|n|<L^2$ for every $n\in T$, and let $P$ be a finite set of primes. Suppose every $p\in P$ satisfies $p>L$ and divides at least one $n\in T$. Then $$|P|\le|T|.$$

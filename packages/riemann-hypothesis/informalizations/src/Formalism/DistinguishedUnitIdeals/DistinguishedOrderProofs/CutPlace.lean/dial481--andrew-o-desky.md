---
{
  "module": "src/Formalism/DistinguishedUnitIdeals/DistinguishedOrderProofs/CutPlace.lean",
  "declarations": [
    "Formalism.ExponentWindows.exists_cuts_of_sparse_thick"
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

## Cuts in a cyclic set with a sparsity condition

[Theorem ALG.0965](https://andrewodesky.com/rh/lean/Formalism.ExponentWindows.exists_cuts_of_sparse_thick/)

Let $n\ge1$ and $j\ge1$ satisfy $j+1\le n$, and let $A\subseteq\mathbb Z/n\mathbb Z$. Suppose that for every $a\in A$ and $1\le k,k'\le j$, $$a-k\in A\quad\Longrightarrow\quad a-k-k'\notin A.$$ There are a nonempty set $C\subseteq\mathbb Z/n\mathbb Z$ and integers $\ell_c\ge0$ for $c\in\mathbb Z/n\mathbb Z$ such that every $c\in C$ satisfies:

1. $c+k\notin A$ for $1\le k\le j$.
2. $j\le\ell_c\le3j+1$ and $\ell_c\le n$.
3. $c-\ell_c\in C$, and $c-k\notin C$ for $1\le k<\ell_c$.
4. If $0\le k<\ell_c$ and $c-k\in A$, then $k\le j$.
5. At most two integers $k\in[0,\ell_c)$ satisfy $c-k\in A$.
6. If $0\le k,k'<\ell_c$ and $c-k,c-k'\in A$, then $|k-k'|\le j$.

All additions and subtractions of elements of the cyclic group are modulo $n$.

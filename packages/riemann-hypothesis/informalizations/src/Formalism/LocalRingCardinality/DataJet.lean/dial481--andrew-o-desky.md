---
{
  "module": "src/Formalism/LocalRingCardinality/DataJet.lean",
  "declarations": [
    "Formalism.BasicNotions.JetLoc",
    "Formalism.BasicNotions.JetLoc1",
    "Formalism.BasicNotions.ThetaJet"
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

## Local formal theta series

[Definition / hypothesis PHT.D130](https://andrewodesky.com/rh/lean/Formalism.BasicNotions.ThetaJet/)

Hypothesis (local formal theta series). Use the field $E$, finite abelian group $A$, ranks $m,N_j=k+j(t+1)$ and prime classes in ([Family fields and Galois data](https://andrewodesky.com/rh/lean/Formalism.HC.Frame/)). Choose two index sets $I,I_1$.

For each $a\in I$, choose a prime $\ell_a\ge5$, an even integer $d_a\ge2$, nonnegative integers $n_a^0,n_a^1$ and a formal power series $$\Theta_a\in\mathbb C_{\ell_a}[[X_{s,u,v}:s\in\mathbb Z/d_a\mathbb Z,\ 0\le u<n_a^0,\ 0\le v<n_a^1]].$$ Choose a stage $j_a$ with $1\le j_a\le m$, $n_a^0=N_{j_a-1}$ and $n_a^1=N_{j_a}$. Require $\ell_a$ to belong to the signal or inert prime class.

For each $a\in I_1$, choose a prime $\ell_a\ge5$, nonnegative integers $n_a^0,n_a^1$ and a formal power series with the same definition but with cyclic index set $\mathbb Z/1\mathbb Z$. Choose $1\le j_a\le m$, $n_a^0=N_{j_a-1}$ and $n_a^1=N_{j_a}$. Require $\ell_a$ to lie in the inert prime class and require the following even-order assertion to fail: for every prime ideal of $\mathcal O_E$ above $\ell_a$ and every arithmetic Frobenius at that prime, the $A$-coordinate under the fixed Galois identification has even order.

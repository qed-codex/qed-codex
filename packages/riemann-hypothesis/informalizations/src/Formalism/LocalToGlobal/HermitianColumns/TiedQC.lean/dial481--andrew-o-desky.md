---
{
  "module": "src/Formalism/LocalToGlobal/HermitianColumns/TiedQC.lean",
  "declarations": [
    "Formalism.L2.Herm.TwChTied"
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

## Twisted Hermitian column levels

[Definition / hypothesis ARAK.D168](https://andrewodesky.com/rh/lean/Formalism.L2.Herm.TwChTied/)

Use ([Hecke characters in recursive realizations](https://andrewodesky.com/rh/lean/Formalism.L2.Host.CharFrame/)), ([Identifications for arithmetic family members](https://andrewodesky.com/rh/lean/Formalism.MainNotions.N.LocTie/)), ([Hermitian column levels and local modifications](https://andrewodesky.com/rh/lean/Formalism.L2.Herm.HermColsCh/)) and ([Symmetric finite levels and column identifications](https://andrewodesky.com/rh/lean/Formalism.L2.Forms.FormsTiedSym/)). Keep their chosen character $\xi_\mu$, untwisted and twisted column chains, base twist $\mu_0$, and fixed Hermitian spaces $X_i$. Define $$Q_\mu=\{v\text{ a finite }F\text{-place}:\xi_\mu\text{ is ramified at some finite }E\text{-place above }v\}.$$ Ramified means nontrivial on the local unit group.

Hypothesis (twisted classes and levels). For each source $u$ and twist $\mu$, choose a bijection $eC_0$ from untwisted to twisted initial classes and group isomorphisms of their prescribed stabilizers. For every $i\le m$ choose a bijection $eY_i$ of their value sets, preserving the recorded determinant factors. The given initial twisting map carries a function $\varphi$ to the function with value $\varphi(c,y)$ at $(eC_0(c),eY_0(y))$. The set $Q_\mu$ is finite.

Choose finite branch-label sets $\mathcal B_{u,\mu,i}$ at every stage, with $\mathcal B_{u,\mu,m}$ a singleton, and maps from twisted classes to their branch labels. For every $1\le i\le m$ and branch choose a finitely generated full integral coordinate lattice $\Lambda$ with $$T_u\Lambda^\#\subset\Lambda,\qquad[\Lambda^\#:\Lambda]=T_u^{2f},$$ and local subgroups $U_v$ of its unitary stabilizers. Outside $Q_\mu$ and $g_0g_1T_u$ they are full stabilizers. At $v\mid g_a$ they contain the stabilizer elements satisfying $(x-1)\Lambda_v\subset g_a\Lambda_v$. At $v\mid T_u$ they are exactly the stabilizer elements acting trivially on $(\Lambda^\#)_v/\Lambda_v$. At every $v\in Q_\mu$ there exists a positive integer $b$ such that all stabilizer elements with $(x-1)\Lambda_v\subset b\Lambda_v$ belong to $U_v$. The adelic subgroup $U$ is exactly the unitary finite adelic matrices whose components belong to these $U_v$.

At every twisted class and every stage choose an $\mathcal O_E$-submodule of $X_i$. For $\mu\ne\mu_0$, $1\le i\le m$ and each branch, require the double-quotient, completed-class-lattice and injective-stabilizer-image conditions of ([Hermitian column levels and local modifications](https://andrewodesky.com/rh/lean/Formalism.L2.Herm.HermColsCh/)) for these chosen lattices and branch levels.

At stage $m-1$ choose a common level satisfying the same lattice and local subgroup conditions. Choose a finite set $Y_b$ with an action of its adelic group, and points $y_\beta$ indexed by branches. Every element of $Y_b$ belongs to the orbit of exactly one $y_\beta$. The branch base lattices all equal the common base lattice; every branch adelic group is contained in the common group and is exactly the stabilizer of $y_\beta$.

Hypothesis (comparison with untwisted branches). Choose a map $g$ from each twisted branch to an untwisted branch at the same source and stage. Their completed base lattices agree at every $v\notin Q_\mu$. Their local groups agree there whenever either $i+1\ne m$ or $v\nmid g_0g_1$. Every $v\in Q_\mu$ divides none of $T_u,g_0,g_1$, at every source.

At $\mu_0$, the chosen initial class bijection and all value-set bijections are exactly the identifications induced by the prescribed equality of twisted and untwisted column chains. Every twisted determinant discriminant constant equals the untwisted constant at the fixed source $u_0$.

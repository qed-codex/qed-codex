---
{
  "module": "src/Development/AutomorphicArithmetic/AutomorphicVarieties/HeightAndVanishing/CountZ.lean",
  "declarations": [
    "UpperTheory.V.HV.countZ"
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

## Automorphic and cohomological inputs for localization bounds

[Theorem GC.1745](https://andrewodesky.com/rh/lean/UpperTheory.One.Join.automorphic_window_of_inputs/)

Assume ([Galois representations of polarized cusp forms](https://andrewodesky.com/rh/lean/UpperTheory.Gal.Int.galoisLocalGlobalStrong_recParameter/)), with all its local comparison hypotheses and conventions, and ([Base change from a definite unitary group](https://andrewodesky.com/rh/lean/UpperTheory.BaseChangeIdentities.baseChangeN/)). Then the following assertions hold.

1. The condition in ([Normalized Poitou–Tate duality for finite Galois modules](https://andrewodesky.com/rh/lean/GlobalTheory.Published.PoitouTateDuality/)), ([Local cohomology finiteness and dimension](https://andrewodesky.com/rh/lean/CompanionTheory.LocalTateOrthogonality.Gcoh.top_locfin/)), ([Local Tate duality](https://andrewodesky.com/rh/lean/CompanionTheory.LocalTateOrthogonality.Gcoh.top_tate/)), ([Class-group ranks in cyclotomic towers](https://andrewodesky.com/rh/lean/UpperTheory.V.FW.ferreroWashington/)), and the existence of a real constant satisfying the condition in ([A uniform bound for second cyclotomic cohomology](https://andrewodesky.com/rh/lean/UpperTheory.V.LemmaK/)) all hold, with the quantifiers and normalizations specified by these titles.
2. All five uniform character estimates I, II, III, V and Z in the conventions of ([Positive localization lengths from character estimates](https://andrewodesky.com/rh/lean/UpperTheory.V.HV.pointHV_of_counts/)) hold, including their case conditions, finiteness assertions, quantifiers and dependence of constants. The Poitou–Tate, local finiteness, local Tate duality and second-cohomology hypotheses of ([Positive localization lengths from character estimates](https://andrewodesky.com/rh/lean/UpperTheory.V.HV.pointHV_of_counts/)) also hold.
3. The universal Bernoulli character-eigenspace hypothesis in the conventions of ([Summing the negative localization lengths](https://andrewodesky.com/rh/lean/UpperTheory.V.Odd.thmBcFree_of/)) holds, with its coefficient rings, parity, integrality condition and valuation normalization.

The condition in ([Window condition: a bound on the Tate-Shafarevich groups of the twists Q\_l/Z\_l(-k) over auxiliary abelian fields](https://andrewodesky.com/rh/lean/UpperTheory.Top.VWin/)) also holds.

## Vanishing of the Selmer group of the twist Q\_l/Z\_l(-e) for even e with l - 1 dividing 2e

[Theorem GC.1.1779](https://andrewodesky.com/rh/lean/UpperTheory.V.X.propZ/)

For an algebraic closure $\Omega$ of $\mathbb Q$ write $G=\operatorname{Gal}(\Omega/\mathbb Q)$, with its Krull topology, and write $I_A\subset D_A\subset G$ for the inertia group and the decomposition group of a valuation subring $A$ of $\Omega$. For a prime $\ell$ let $\epsilon_\ell:G\to\mathbb Z_\ell^\times$ be the $\ell$-adic cyclotomic character. A *coefficient ring* for $\ell$ is a discrete valuation ring $\mathcal O\subset\overline{\mathbb Q}_\ell$ that contains $\mathbb Z_\ell$ and is a finitely generated $\mathbb Z_\ell$-module.

**Theorem.** Let $\Omega$ be an algebraic closure of $\mathbb Q$, $\ell\ge5$ a prime, $\mathcal O$ a coefficient ring for $\ell$, and $e\ge2$ an even integer such that $\ell-1$ divides $2e$. Let $M$ be the $\mathcal O$-module $\mathcal O\otimes_{\mathbb Z_\ell}(\mathbb Q_\ell/\mathbb Z_\ell)$ with the discrete topology, on which $G$ acts by $g\cdot m=\epsilon_\ell(g)^{-e}m$. Let $c$ be a class in the first continuous cohomology group $H^1(G,M)$ that satisfies the following two conditions.

1. The restriction of $c$ to $I_A$ is zero for every valuation subring $A$ of $\Omega$.
2. The restriction of $c$ to $D_A$ is zero for every valuation subring $A$ of $\Omega$ whose maximal ideal contains $\ell$.

Then $c=0$.

**Corollary (Estimate Z).** For every primitive Dirichlet character $\chi$ there is a natural number $C$ with the following property. Let $(\nu,q,d)$ be an auxiliary triple for $\chi$, with modulus $N$, and let $t\ge0$ be an integer such that $q$ and $d$ are both larger than each of the six numbers $$2t+1,\qquad N_\chi,\qquad o,\qquad p_K,\qquad h_K,\qquad p_1.$$ Let $\Omega$ be an algebraic closure of $\mathbb Q$, $\ell\notin\mathcal B_\chi$ an odd prime, $\mathcal O$ a coefficient ring for $\ell$, and $e$ an integer with $0<e<t$ such that $\ell-1$ divides $2e$ and the trivial character modulo $N$ belongs to $\mathscr X_{\mathcal O}(e)$. Then the Selmer length $L$ of $\epsilon_\ell^{-e}$ formed with $\mathcal O$ and $N$ is finite, and $$\frac L{e_{\mathcal O}}\,\log\ell\le(\ell Ne)^C.$$

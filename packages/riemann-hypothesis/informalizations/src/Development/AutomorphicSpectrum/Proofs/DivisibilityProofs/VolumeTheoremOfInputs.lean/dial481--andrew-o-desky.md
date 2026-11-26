---
{
  "module": "src/Development/AutomorphicSpectrum/Proofs/DivisibilityProofs/VolumeTheoremOfInputs.lean",
  "declarations": [
    "GlobalTheory.CompanionTheory.Ar.Cusp.volumeTheoremX_of_inputs"
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

## Uniform volume and slope bounds for root towers over unitary moduli schemes, from ten geometric inputs

[Theorem ARAK.1.1763](https://andrewodesky.com/rh/lean/GlobalTheory.CompanionTheory.Ar.Cusp.volumeTheoremX_of_inputs/)

Assume the following three groups of statements.

1. The fifteen assertions of “Global hypotheses for arithmetic towers”.
2. The six assertions of ([Six geometric assumptions for the tower volume bound](https://andrewodesky.com/rh/lean/GlobalTheory.CompanionTheory.Ar.Cusp.NineGeoU/)); the first of them asserts the existence of the two real constants $C_h$, $C_u$ named there.
3. The three assertions of ([Three further assumptions for the tower volume bound: integrability, the Weil pairing and comparison under automorphisms](https://andrewodesky.com/rh/lean/ReciprocityTheory.ChartRestriction.G.Geo.PtsIntegrableStatement/)).

Then there is a real number $C\ge0$ with the following property. Let $E$ be a CM field that is an abelian Galois extension of $\mathbb Q$. Take a CM host for $E$, a polarized lattice datum of signature $(p,q)$, a family of moduli schemes, a level $l$, a coefficient field $K$ and a model $Y$ of the moduli scheme of level $l$ over $\mathcal O_K$, as in ([Global models of unitary moduli schemes and geometric origins of root towers](https://andrewodesky.com/rh/lean/GlobalTheory.CompanionTheory.Ar.Top.IsGlobal/)); let $\Psi$, $N=p+q$, $M'$, $\operatorname{rd}_E$ and $\mathcal L_E$ be as defined there. Let $T$ be a root tower for $(\Psi,N)$ with a geometric origin over $Y$ that is good, and let $I$ be an intersection system. Suppose that

- $Y$ is global, the origin satisfies the two extra conditions, and $I$ is full;
- $q\ge1$ and $3q+1\le N$;
- the set $S_0$ of the tower has at most $4\,|\Psi|\,N^2$ elements.

Then, in the notation of ([Root towers, their volumes and their slopes](https://andrewodesky.com/rh/lean/GlobalTheory.CompanionTheory.Ar.Top.RootModel/)), the tower $T$

1. is proportional;
2. has equal volumes;
3. satisfies the limit condition for $I$;
4. satisfies the monomial expansion for $I$;
5. satisfies the intersection lower bound for $I$ with constants $(C,\operatorname{rd}_E,\mathcal L_E)$;
6. satisfies the mean slope lower bound for $I$ with constants $(C,\operatorname{rd}_E,\mathcal L_E)$.

Written out, with $d=|\Psi|N(N-1)/2$, the last two conclusions are the inequalities $$-\,C\,(d+1)\,V\,D(u)\,\mathcal B(B,u)\ \le\ P_B(\ell_u^{\,d+1}),\qquad -\,C\,\mathcal B(B,u)\ \le\ \frac1{|\mathcal C|}\sum_{c\in\mathcal C}\mu_{B,c}(u),$$ $$\mathcal B(B,u)=\bigl(\log(B\operatorname{rd}_E)+|\mathcal L_E|\bigr)\,\|u\|_1+\min(p,q)\sum_{\tau\in\Psi}\Bigl(\max_iu_{\tau,i}-\min_iu_{\tau,i}\Bigr),$$ for every admissible pair $(u,g)$ and every natural number $B$ with $B\ge128$, $4|\Psi|N^2\bigl(1+\|u\|_\infty/g\bigr)<B+1$ and $|S_0|\le B$.

---
{
  "module": "src/Development/AbelianVarietyTheory/Definitions/AutomorphicMembership/MovedReadingSameMapsBaseReadingAgrees.lean",
  "declarations": [
    "GlobalTheory.Mem.Top.Bl.RXs"
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

## Conditions on linked records for the period identity

[Definition / hypothesis THETA.D063](https://andrewodesky.com/rh/lean/GlobalTheory.Fam.BundlePointConditions/)

We use the points, attached records and links of ([The norm bound at the primes 2 and 3 for the families produced by the construction with a given parameter](https://andrewodesky.com/rh/lean/GlobalTheory.Fc.RL.LinkedAt/)) and the datum of ([Datum of the construction and objects over it](https://andrewodesky.com/rh/lean/GlobalTheory.EX.OB.Obj/)). An attached record contains a row-side family, spectral data and a realisation. The following conditions refer to their components.

**Conditions at a linked record.** The ten conditions are:

1. There is a record joining the realisation to the spectral data. It contains coordinate isomorphisms and maps, and five compatibility conditions on chains, rows, norms and pairings (not expanded).
2. For every word $u$ and every used tuple $t$, the embedded value of the row-side pairing at $x,F$ equals the corresponding column period evaluated at the images of $x$ and $F$. The maps and the criterion for a tuple to be used are not expanded.
3. There are four families of lattices and four families of finite-adelic invertible matrices satisfying a frame predicate and diagonal normal-frame conditions at a finite set of places (those conditions are not expanded).
4. There are a group element and a real number satisfying two level and evaluation compatibility conditions (not expanded).
5. The eight existence assertions in ([Analytic theta maps and primitive row comparisons](https://andrewodesky.com/rh/lean/Formalism.IndefR.Links.RealDat.ExAt/)) hold for this realisation, with its other specified maps fixed.
6. The primitive row comparisons in ([Analytic theta maps and primitive row comparisons](https://andrewodesky.com/rh/lean/Formalism.IndefR.Links.RealDat.ExAt/)) hold. The underlying rational family also satisfies the type-separation condition in conclusion (B) of ([Properties of the theta maps of a realised rational family: Hecke equivariance, inner product identities, rationality, and separation of Hecke types](https://andrewodesky.com/rh/lean/GlobalTheory.Closing3.primRows3_typesSep3_alt/)).
7. A finite spectral condition holds: it has ten clauses, including bijectivity of specified maps, finite-dimensionality, finite fibres, independence of pairings and positivity of two volumes. Its maps and other predicates are not expanded.
8. For each place $v$ of the spectral data, if the Boolean labels of indices $a,b$ differ, then $|\lambda_v(a)-\lambda_v(b)|\ge100r^4$, where $r$ is a natural number of the datum.
9. There is a natural number $N\ge\operatorname{rankX}'+1$ such that, for every embedding $\tau$ and adjacent indices $i,i+1<m$, the associated numbers satisfy $$b_\tau(i+1)-b_\tau(i)\ge t+2N^3+1.$$
10. A further natural number $r_S$ of the datum satisfies $r_S\ge1$.

**Diagonal estimate hypothesis.** For every choice of real constants $C_g,c_b,C_u,c_T,C_T$ with $c_b,c_T>0$, there are $C,C'_0,C_{\ell,0}$ with $C\ge1$ such that for every $C'\ge C'_0$, $C_\ell\ge C_{\ell,0}$, datum $D$, real $L$ and source $z$ of $D$, the following implication holds. If $D$ satisfies the standing conditions of the diagonal estimate at scale $L$ with constants $(C',C_\ell,C_g,c_b,C_u,c_T,C_T)$, then the normalized Gram operator $K_z$ of $z$ satisfies $$\bigl\|K_z-\mathrm{id}\bigr\|_{\rm HS}^2\le 4\bigl(e^{C m^5 f L}+1\bigr)\frac{d_z^{\,2}}{D_*}+\bigl(4e^{-k f\log(k)/2}+2e^{-k f\log(k)}\bigr)d_z.$$ The operator $K_z$, the numbers $d_z$, $D_*$, $k,m,f$ and the standing conditions are defined in ([Normalized Gram operators and the standing conditions of the diagonal estimate](https://andrewodesky.com/rh/lean/Formalism.MainNotions.S.Kmat/)). This hypothesis is the conclusion of ([Hilbert-Schmidt bound for the normalized Gram operator of a source, assuming the Siegel-Weil formula](https://andrewodesky.com/rh/lean/GlobalTheory.Core.Rk.rowDiag_of_siegelWeilUnitary/)).

**Realisation witness.** At every context and every point specified by a base, frame, twist data, column input, later stages, object and a witness for the chosen construction parameters, there is required to be a record of compatible realisations. It contains a common family of maps agreeing with the maps already chosen, complex linear equivalences, compatibility with forms and coordinates, vanishing conditions, and further canonicity, rank and standardness conditions. Its constituent predicates are not expanded.

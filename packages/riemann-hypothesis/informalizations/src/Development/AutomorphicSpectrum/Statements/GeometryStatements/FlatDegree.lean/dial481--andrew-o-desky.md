---
{
  "module": "src/Development/AutomorphicSpectrum/Statements/GeometryStatements/FlatDegree.lean",
  "declarations": [
    "GlobalTheory.CompanionTheory.Ar.Fl.FlatDegree"
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

## Six geometric assumptions for the tower volume bound

[Definition / hypothesis ARAK.D099](https://andrewodesky.com/rh/lean/GlobalTheory.CompanionTheory.Ar.Cusp.NineGeoU/)

The following six assertions are used in the tower volume bound.

**(1) Geometric height and mean estimates.** There are real numbers $C_h,C_u$ such that, for every abelian CM field $E/\mathbb Q$ and every choice of the associated geometric data, compactification origin, cusp weight $U$, model and tied bounded regularisation satisfying the prescribed conditions (not expanded), all three conclusions below hold. Write $f,N,j'$ and $K_A$ for the numbers attached to those data, $\operatorname{rd}_E$ for the root discriminant and $\ell$ for the real logarithmic derivative attached to the data. Put $R_B=\log(B\operatorname{rd}_E)+|\ell|$.

- For every $B,a,b\in\mathbb N$ with $B\ge4f+2$ and $1\le a\le b$, there is $t_0>0$ such that for $0<t\le t_0$ the regularised metric indexed by $B,a,b,t$ is semipositive, nef on fibres and ample on the generic fibre.
- For every $B,a,b\in\mathbb N$ with $B\ge4fN^2$ and $1\le a\le b$, there is $t_0>0$ such that for $0<t\le t_0$ and every arithmetic-variety point ideal containing the coordinate ideal, its height $h_t$ satisfies $$h_t\ge -C_h f j'R_B-\frac ab K_A.$$
- If $j'\ge1$ and $3j'+1\le N$, then for every $B\ge4fN^2$ the normalised integral $m(U)$ satisfies $m(U)\le C_u f j'R_B$.

The geometric data, admissibility conditions, metric, height and normalised integral are not expanded.

**(2) Flag Chern comparison.** For every CM field and associated moduli and Hodge compactification data, every arithmetic coordinate variety of dimension $d+1$, every flag with two specified levels, and every $p$ in the prescribed finite set outside the second exceptional set, assume the Hodge-freeness condition, $p\ne2$ and $p\nmid\operatorname{disc}(E)$. For each prescribed Frobenius permutation and each place over $p$ of each integral closure of $\mathbb Z$ in the ambient field, the flag Chern comparison holds. It equates, for every label $\tau$, $k\ge1$ and list $Q$ of length $d+1-k$, a $k$th flag intersection number to the evaluation on the divisor of $p$ of a polynomial determined by the Frobenius permutation and the flag. The two-level condition, local places, polynomial coefficients and intersection evaluations are not expanded. The quantifier over $p$ does not separately require $p$ to be prime.

**(3) Triviality of flags.** For every CM field and associated moduli and Hodge compactification data, every arithmetic coordinate variety, every flag and root-line data satisfying the prescribed condition, and every $p$ in the finite set at which Hodge-freeness holds, the following holds at every place over $p$: on each relevant irreducible component of the special fibre, the prescribed flag has a frame in a scaled trivial bundle after extending the residue field. The root-line, relevance and flag-frame conditions are not expanded.

**(4) Degree of flat generators.** For every CM field $E$, associated moduli data, Kronecker character $\chi$ of nonzero modulus $d$, suitable flat generator and compatible norms, the norms are adelic and their degree equals $$\frac{p-q}{2}\left(\gamma+\log\frac{2\pi}{\operatorname{rd}_E}-\operatorname{Re}\frac{L'(1,\chi)}{L(1,\chi)}\right)+q\left(2\log\sqrt d-\log\operatorname{rd}_E\right).$$ The generator, compatibility and normalisation of degree are not expanded. Division by zero is defined to be zero.

**(5) Automorphisms of twists.** For every CM field and associated datum, level and moduli object, every automorphism of the auxiliary field data admits a compatible twisting isomorphism. For each such isomorphism there is a compatible automorphism of the moduli object over its base and a map from the twisted universal object to the original one. The compatibility conditions are not expanded.

**(6) Comparison of intersection limits.** For every full intersection system and two coordinate pullbacks from a common arithmetic variety, suppose the block maps, homogeneous polynomial, realisations, algebraicity and common-singularity conditions hold (not expanded). For every list of $D+1$ line indices, the difference between the two regularised intersection evaluations, each multiplied by the relative degree of the corresponding coordinate function field over the common function field, tends to zero as the regularisation parameter tends to $0$ from above. The realisations and intersection evaluations are not expanded.

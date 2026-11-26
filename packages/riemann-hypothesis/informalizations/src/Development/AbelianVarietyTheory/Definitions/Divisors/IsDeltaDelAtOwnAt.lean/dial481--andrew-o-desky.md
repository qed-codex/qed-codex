---
{
  "module": "src/Development/AbelianVarietyTheory/Definitions/Divisors/IsDeltaDelAtOwnAt.lean",
  "declarations": [
    "GlobalTheory.BigOn.CoreTies"
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

## Compatibility conditions for covolume points

[Definition / hypothesis ARAK.D170](https://andrewodesky.com/rh/lean/GlobalTheory.BigTop.PtAt.CompatibilityConditions/)

Hypothesis (compatibility conditions for covolume points). Use ([Compatible points for arithmetic covolume bounds](https://andrewodesky.com/rh/lean/GlobalTheory.BigTop.PtAt/)) and ([Coefficient fields for covolume comparisons](https://andrewodesky.com/rh/lean/GlobalTheory.FinalJoin2.FieldOK0/)) for the same arithmetic member and height constant. Impose ([Canonical integral modules for original moduli](https://andrewodesky.com/rh/lean/Formalism.L2.Pj.LawsM.pins/)), ([Integral evaluation of moduli sections](https://andrewodesky.com/rh/lean/Formalism.L2.Pj.LawsM.evalWD/)), ([Original moduli uniformizations and cusp norms](https://andrewodesky.com/rh/lean/Formalism.L2.Pj.LawsM/)), and ([Isotropic lattices and Fourier exponents](https://andrewodesky.com/rh/lean/Formalism.L2.Pj.FJ.LatZ/)) on its original moduli realization. Every natural stage, including stages outside $1,\ldots,m$, has positive polarized-module rank.

Require ([Compatibility of recursive coordinate realizations](https://andrewodesky.com/rh/lean/Formalism.IndefR.IndefiniteRealisation/)), using ([Linked arithmetic and theta realizations](https://andrewodesky.com/rh/lean/Formalism.L2.TiedDataSKAlt/)) and ([Spectral column and period realizations](https://andrewodesky.com/rh/lean/Formalism.L2.SG.HidaSetting.HidaSetting/)). Reconstruct the point from those choices, its selected columns and periods, its values of $\Delta,h_0$, and its stabilizer divisibilities. The reconstructed point equals the chosen point, including every chosen object and comparison.

The two chosen quadratic primes above $g_0,g_1$ in the original moduli realization equal the primes in ([Hecke characters in recursive realizations](https://andrewodesky.com/rh/lean/Formalism.L2.Host.CharFrame/)). The original level ideal is the product of the prime ideals in the analytic generator-place set. The conjugate of each fixed norm-$g_i$ error generator belongs to the extension of the corresponding chosen quadratic prime. Both fixed auxiliary Hecke characters take all values in $F_O=\mathbb Q(\jmath(O))$.

At every nonbase coefficient place $w$ put $p_D(w)=p'_\Delta$ when its residue characteristic is $p_\Delta$, and $p_D(w)=p_\Delta$ otherwise. For each of these two excluded rational primes choose a prime of the quadratic subfield above it, using the same choice for every $w$ with that $p_D(w)$. Its extension to $E$ is contained in every auxiliary prime of the selected tuple above $p_D(w)$.

Impose ([Analytic theta maps and primitive row comparisons](https://andrewodesky.com/rh/lean/Formalism.IndefR.Links.RealDat.ExAt/)), ([Integral frames and Hecke operator laws](https://andrewodesky.com/rh/lean/Formalism.L2.DIV.DefFam3.Ok3/)), ([Divisor rows and additive-character comparisons](https://andrewodesky.com/rh/lean/Formalism.L2.DIV.DivisionCompatibilityDataThreeSided/)), ([One-map and geometric comparison laws](https://andrewodesky.com/rh/lean/Formalism.IndefR.FWT.FWTie/)), ([Geometric theta class evaluations](https://andrewodesky.com/rh/lean/Formalism.IndefR.FWT.OMPins/)), and ([Scalar normalizations and series comparisons](https://andrewodesky.com/rh/lean/GlobalTheory.SeriesTie.ExportTie/)). In particular, at each good coefficient embedding evaluation against the chosen extremal vector is injective. At each other coefficient embedding a unit vector evaluates to the complex conjugate automorphic form. At each stage a rational action of the finite group on cusp forms preserves the integral lattice and realizes its complex action multiplied by its designated character. The extremal vector, expressed as a tuple of lowest-type vectors, pairs with a unit coefficient vector to the explicit determinant polynomial in ([Analytic theta intertwiners and Weil actions](https://andrewodesky.com/rh/lean/Formalism.IndefR.Links.RealDat.IsChainW/)).

Any two different occurring base Hecke types, including their inert eigenvalues, remain distinguished at every lifted stage: their transported types differ either on an allowed split Hecke operator or on an allowed inert operator. The member's designated distinguished dimension is the dimension of the selected base-tuple rational row subspace in principal-level coordinates, as defined in ([Class sums and finite Hecke families](https://andrewodesky.com/rh/lean/Formalism.L2.DIV.CSD/)).

Every nonzero local defect is supported in the designated twisted-place set. More explicitly, if for some stage either base image index at $w$ or $\bar w$, either local determinant index of the selected base lattice at $w$ or $\bar w$, or either local error allocation at $w$ or $\bar w$ is nonzero, then $w$ belongs to that twisted set.

The chosen subgroup equals the subgroup used by the theta expansions. The inverse of its selected principal-level character has values represented by elements of the embedded base field $K_0$; the oriented coefficient embeddings of these elements are the specified theta-expansion characters for every twist index and side. Every theta-expansion input vector transforming under that subgroup by this character belongs to the selected expansion-input set. The field $K_0\subset K$ is the chosen intermediate coefficient field of ([Identifications for arithmetic family members](https://andrewodesky.com/rh/lean/Formalism.MainNotions.N.LocTie/)); it is separate from the field $F_O$ generated by the integral ring image.

For every nonbase coefficient place, all values of its local twisting Hecke character, with zero absolute-value twist, lie in the designated embedded base field $K_0$. That field contains a copy of the ray class field of the chosen quadratic field of modulus $g_0g_1p_\Delta p'_\Delta$, extending the given quadratic-field embedding. It contains every root of $z^{g_i(g_i-1)}=1$ for $i=0,1$.

For a tuple $t$, put $$M_t=g_0g_1\prod_{q\in\{NP:P\in Q_t\}}q,$$ using each distinct residue cardinality once. Under the fixed quadratic-field embedding into $K$, every prime ideal $\mathfrak P$ of $K$ not containing $M_t$, with contraction $\mathfrak p$, admits $a\in\mathbb N$ and $\alpha\in\mathcal O_{E_0}$ satisfying $$N\mathfrak P=(N\mathfrak p)^a,\qquad \mathfrak p^a=(\alpha),\qquad \alpha\equiv1\pmod{M_t}.$$

Impose the memberwise conditions in ([Integral twisting conditions for arithmetic families](https://andrewodesky.com/rh/lean/Formalism.MainNotions.TwIn/)) with the effective twist character replaced by every integer power $\Psi^a$ with $\gcd(|a|,\ell)=1$ at each nonbase coefficient place of residue characteristic $\ell$. One choice of all $N_0(i)$ and all finite expansion subsets works simultaneously for every coefficient place and every such power; the error allocations may depend on the power. The conjugate-place twist data and their orientation conditions are also imposed.

Every finite-type label has a selected tuple of generator-place polynomials, using the definition of selected in ([Finite types and idempotents for the family](https://andrewodesky.com/rh/lean/Formalism.BasicNotions.NTypes/)). Thus its polynomial tuple satisfies that definition at both generator primes and for both the selected tame characters and their inverses.

For each level prime $g$ choose a unital multiplicative map $\vartheta:\overline{\mathbb F}_g\to\mathbb C$ which is injective on nonzero elements, and elements $\zeta_e\in\overline{\mathbb F}_g$ for every natural $e$, with $\zeta_e$ of order $g^e-1$ for $e\ge1$, satisfying $\zeta_{eh}^{(g^{eh}-1)/(g^e-1)}=\zeta_e$ for $e,h\ge1$. A monic irreducible polynomial $Q$ with nonzero constant term labels the cuspidal characters in ([Cuspidal characters of finite general linear groups](https://andrewodesky.com/rh/lean/GlobalTheory.greenRegularCharacters_holds/)) by the parameter $\theta_Q(\zeta_e)=\vartheta(\alpha)$, for a root $\alpha$ of $Q$. An irreducible character $\chi$ has label $F$ if it occurs in Harish–Chandra induction of a list of these cuspidal characters whose ranks sum to $r$ and whose polynomials multiply to $F$. The prescribed central idempotents are required to be $$e_F=\sum_{\substack{\chi\text{ irreducible of }G\\\chi\text{ has label }F}}\frac{\chi(1)}{|G|}\sum_{h\in G}\chi(h^{-1})[h],\qquad G=\mathrm{GL}_r(\mathbb F_g),$$ using the prescribed $\vartheta$. Here $[h]$ is the basis element of $\mathbb C[G]$.

For every generator place over $g$ and each stage $j+1$, let $c_{v,j}\in\mathbb F_g^\times$ be its designated tame parameter. The degree-one character determined by $c_{v,j}$ through the chosen $\zeta_1,\vartheta$ is either $\omega_g^{2(j+1)}$ or its inverse, where $\omega_g$ is the chosen injective generator character in ([Hecke characters in recursive realizations](https://andrewodesky.com/rh/lean/Formalism.L2.Host.CharFrame/)). The finite-field embedding $\vartheta$ equals the member’s prescribed one at each generator prime.

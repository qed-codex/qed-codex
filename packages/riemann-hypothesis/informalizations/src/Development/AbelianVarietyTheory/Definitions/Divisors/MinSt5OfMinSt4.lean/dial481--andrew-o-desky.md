---
{
  "module": "src/Development/AbelianVarietyTheory/Definitions/Divisors/MinSt5OfMinSt4.lean",
  "declarations": [
    "GlobalTheory.SiegJoin.MinAt5"
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

## Theta-integral compactifications of a Siegel moduli family and semiabelian covers

[Definition / hypothesis AV.D262](https://andrewodesky.com/rh/lean/GlobalTheory.Poinc.IsThetaCompact/)

Fix integers $g\ge0$ and $n\ge1$, put $R_n=\mathbb Z[\zeta_n,1/n]$ with $\zeta_n=e^{2\pi i/n}$, and let $(A,P,\ell)/U$ be a Siegel moduli family of type $(g,n)$ in the sense of ([Siegel moduli families and their level pairing](https://andrewodesky.com/rh/lean/GlobalTheory.ZM.SFam/)). Let $Z$ be an $R_n$-scheme and $i:U\to Z$ a morphism of schemes.

**Eightfold powers.** Let $W=(W_{ab})\in M_8(\mathbb Z)$, let $T$ be a scheme and $u:T\to U$ a morphism; $T$ is an $R_n$-scheme through $u$. A polarized abelian scheme $(E,\mathcal L)$ over $T$, in the sense of ([Theta systems, their realizations on abelian schemes, and rational models](https://andrewodesky.com/rh/lean/GlobalTheory.ZH.ThetaSys/)), is a *$W$-twisted eightfold power of the family along $u$* when there are a level-$n$ family $(A',P',\ell')$ over $T$ with a pullback identification with $(A,P,\ell)$ along $u$, and group homomorphisms $p_1,\ldots,p_8:E\to A'$ over $T$, with these two properties. The map $(p_1,\ldots,p_8):E\to A'\times_T\cdots\times_TA'$ is an isomorphism. And $$\mathcal L\simeq\bigotimes_{a,b=1}^{8}(p_a,p_b)^*P'^{\,\otimes W_{ab}}.$$

**Theta-integral compactifications.** The pair $(Z,i)$ is a *theta-integral compactification* of $U$ when the following hold.

1. $Z$ is normal and projective over $R_n$, and $i$ is an open immersion of $R_n$-schemes with dense image.
2. There is a matrix $W\in M_8(\mathbb Z)$ with $W+W^{\mathsf T}$ positive definite and $\det(W+W^{\mathsf T})=1$ for which the following divisibility holds. Let $(o,\Omega)$ be an arithmetic base, $\mathcal S$ a theta system over $(o,\Omega)$ with ring $R\subseteq\Omega$, and $(E,\mathcal L)$ the polarized abelian scheme of a realization of $\mathcal S$. Let $u:\operatorname{Spec}R\to U$ be a morphism that sends the generic point of $\operatorname{Spec}R$ to the generic point of an irreducible component of $U$, and suppose that $(E,\mathcal L)$ is a $W$-twisted eightfold power of the family along $u$. Let $M$ be a normal rational model of $\Omega$ over $o$, and let $\pi_M:M\to Z$ be a morphism of schemes whose composite with $\operatorname{Spec}\Omega\to M$ is $$\operatorname{Spec}\Omega\longrightarrow\operatorname{Spec}R\xrightarrow{\ u\ }U\xrightarrow{\ i\ }Z.$$ Then the theta constants of $\mathcal S$ are divisible on $M$.

Theta systems, realizations, arithmetic bases, rational models and divisibility of theta constants are defined in ([Theta systems, their realizations on abelian schemes, and rational models](https://andrewodesky.com/rh/lean/GlobalTheory.ZH.ThetaSys/)).

**Semiabelian covers.** Let $L$ be a line bundle on $Z$. A *semiabelian cover* of $(Z,i,L)$ consists of

- a finite injective ring homomorphism $R_n\to o'$ and a normal scheme $S'$, projective over $o'$;
- a dense open subscheme $V\subseteq S'$ and a finite surjective morphism $c:V\to U$;
- a proper surjective morphism $q:S'\to Z$ with $q|_V=i\circ c$, compatible with the structure maps to $\operatorname{Spec}o'$ and $\operatorname{Spec}R_n$;
- a semiabelian scheme $G'\to S'$, in the sense of ([Abelian and semiabelian group schemes](https://andrewodesky.com/rh/lean/ReciprocityTheory.ChartRestriction.G.Semi.IsAbelianScheme/)), smooth of relative dimension $g$, with a group pullback identification of $c^*A$ with $G'|_V$;
- an integer $N\ge1$ with $$q^*L\simeq\omega_{G'}^{\otimes N},\qquad\omega_{G'}=\det\bigl(e_{G'}^*\Omega^1_{G'/S'}\bigr).$$

The triple $(Z,i,L)$ is a *theta-integral compactification with a semiabelian cover* when $(Z,i)$ is a theta-integral compactification of $U$, the scheme $Z$ is Noetherian, $L$ is ample, and $(Z,i,L)$ has a semiabelian cover.

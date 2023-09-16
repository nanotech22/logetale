function copyClipboard(id) {
    if (id == "logprodfmla") {
        var text = `@ARTICLE{name,
author = {{Herr}, Leo},
title = "{The log product formula}",
journal = {Algebra \& Number Theory},
keywords = {Mathematics - Algebraic Geometry},
year = 2023,
volume = {17},
doi = {10.2140/ant.2023.17.1281}

}`;
    }


    if (id == "logprodfmlaqkthy") {
    var text = `@article{name, 
title={The Log Product Formula in Quantum K-theory}, 
volume={175}, 
DOI={10.1017/S0305004123000063}, 
number={2}, 
journal={Mathematical Proceedings of the Cambridge Philosophical Society}, 
author={Chou, You–Cheng and Herr, Leo and Lee, Yuan–Pin}, 
year={2023}, 
pages={225–252}}`;
    }




    if (id == "loghochschild") {
var text = `@ARTICLE{name,
author = {{Hablicsek}, M{\'a}rton and {Herr}, Leo and {Leonardi}, Francesca},
title = "{Logarithmic Hochschild co/homology via formality of derived intersections}",
journal = {arXiv e-prints},
keywords = {Mathematics - Algebraic Geometry},
year = 2023,
month = aug,
eid = {arXiv:2308.09447},
pages = {arXiv:2308.09447},
doi = {10.48550/arXiv.2308.09447},
archivePrefix = {arXiv},
eprint = {2308.09447},
primaryClass = {math.AG},
adsurl = {https://ui.adsabs.harvard.edu/abs/2023arXiv230809447H},
adsnote = {Provided by the SAO/NASA Astrophysics Data System}
}

`;
    }



    if (id == "costello") {
var text = `@article{name,
title={Costello’s pushforward formula: errata and generalization},
author={Leo Herr and Jonathan Wise},
journal={manuscripta mathematica},
year={2021},
volume={171},
pages={621 - 642},
url={https://api.semanticscholar.org/CorpusID:232269743}
}`
    }


    if (id == "costellokthy") {
var text = `@ARTICLE{name,
author = {{Chou}, You-Cheng and {Herr}, Leo and {Lee}, Y. -P.},
title = "{Higher Genus Quantum $K$--theory}",
journal = {arXiv e-prints},
keywords = {Mathematics - Algebraic Geometry},
year = 2023,
month = may,
eid = {arXiv:2305.10137},
pages = {arXiv:2305.10137},
doi = {10.48550/arXiv.2305.10137},
archivePrefix = {arXiv},
eprint = {2305.10137},
primaryClass = {math.AG},
adsurl = {https://ui.adsabs.harvard.edu/abs/2023arXiv230510137C},
adsnote = {Provided by the SAO/NASA Astrophysics Data System}
}
`
    }

    if (id == "defmsmodules") {
var text = `@article{name,
title = {Deformations of modules through butterflies and gerbes},
journal = {Journal of Pure and Applied Algebra},
volume = {224},
number = {1},
pages = {362-387},
year = {2020},
issn = {0022-4049},
doi = {https://doi.org/10.1016/j.jpaa.2019.05.010},
url = {https://www.sciencedirect.com/science/article/pii/S0022404919301288},
author = {Leo Herr},
keywords = {Deformations, Grothendieck topologies, Sheaves, Gerbes, Butterflies},
abstract = {Classifying obstructions to the problem of finding extensions between two fixed modules goes back at least to L. Illusie's thesis. Our approach, following in the footsteps of J. Wise, is to introduce an analogous Grothendieck Topology on the category A-mod of modules over a fixed ring A in a topos E. The problem of finding extensions becomes a banded gerbe and furnishes a cohomology class on the site A-mod. We compare our obstruction and that coming from Illusie's work, giving another construction of the exact sequence Illusie used to obtain his obstruction. Our work circumvents the cotangent complex entirely and answers a question posed by Illusie.}
}`
    }

    if (id == "defmsalgs") {
var text = `@ARTICLE{name,
    author = {{Herr}, Leo},
     title = "{Deformations of Algebras with 2-Extensions}",
   journal = {arXiv e-prints},
  keywords = {Mathematics - Algebraic Geometry, Mathematics - Commutative Algebra},
      year = 2022,
     month = apr,
       eid = {arXiv:2204.12040},
     pages = {arXiv:2204.12040},
       doi = {10.48550/arXiv.2204.12040},
archivePrefix = {arXiv},
    eprint = {2204.12040},
primaryClass = {math.AG},
    adsurl = {https://ui.adsabs.harvard.edu/abs/2022arXiv220412040H},
   adsnote = {Provided by the SAO/NASA Astrophysics Data System}
}

`
    }
    

    if (id == "monogen1") {
var text = `@ARTICLE{name,
author = {{Arpin}, Sarah and {Bozlee}, Sebastian and {Herr}, Leo and {Smith}, Hanson},
title = "{The scheme of monogenic generators I: representability}",
journal = {Research in Number Theory},
keywords = {Mathematics - Number Theory},
year = 2023,
month = jan,
volume = {9},
number = {1},
doi = {10.1007/s40993-022-00419-5},
}`
    }

    

    if (id == "monogen2") {
var text = `@article{name,
author = "Arpin, Sarah and Bozlee, Sebastian and Herr, Leo and Smith, Hanson",
title = "The scheme of monogenic generators II: local monogenicity and twists",
journal = "Research in Number Theory",
year = "2023",
volume = "9",
number = "2",
doi = "10.1007/s40993-023-00449-7",
}
`
    }

    

    if (id == "logjets") {
var text = `@ARTICLE{name,
    author = {{Herr}, Leo},
     title = "{The log tangent space of the log jet space}",
   journal = {arXiv e-prints},
  keywords = {Mathematics - Algebraic Geometry},
      year = 2022,
     month = oct,
       eid = {arXiv:2210.08505},
     pages = {arXiv:2210.08505},
       doi = {10.48550/arXiv.2210.08505},
archivePrefix = {arXiv},
    eprint = {2210.08505},
primaryClass = {math.AG},
    adsurl = {https://ui.adsabs.harvard.edu/abs/2022arXiv221008505H},
   adsnote = {Provided by the SAO/NASA Astrophysics Data System}
}

`
    }



    copyToClipboard(text);
    alert("Copied Bibtex to clipboard!");
}



function copyToClipboard(text) {
    if (window.clipboardData && window.clipboardData.setData) {
        // Internet Explorer-specific code path to prevent textarea being shown while dialog is visible.
        return window.clipboardData.setData("Text", text);

    }
    else if (document.queryCommandSupported && document.queryCommandSupported("copy")) {
        var textarea = document.createElement("textarea");
        textarea.textContent = text;
        textarea.style.position = "fixed";  // Prevent scrolling to bottom of page in Microsoft Edge.
        document.body.appendChild(textarea);
        textarea.select();
        try {
            return document.execCommand("copy");  // Security exception may be thrown by some browsers.
        }
        catch (ex) {
            console.warn("Copy to clipboard failed.", ex);
            return prompt("Copy to clipboard: Ctrl+C, Enter", text);
        }
        finally {
            document.body.removeChild(textarea);
        }
    }
}
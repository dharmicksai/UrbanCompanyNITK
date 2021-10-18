'use strict';

const e = React.createElement;

class Ads extends React.Component {
  constructor(props) {
    super(props);
    this.state = { liked: false };
    
  }

  render() {

    return (
    <div className="card" data-aos = "fade-up" data-aos-delay="300">
      <div className="card-header">
        <div className="card-title-group">
          <h5 className="card-title">Web Club NITK</h5>
          
        </div>
      </div>
      
      <img className="card-image" src = "data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAOEAAADhCAMAAAAJbSJIAAAAwFBMVEUyMjJjmfCu1uhlnfez3O+w2esuLCuy2+1mnvkoIyAxMDAwLCMxMS8nIR4sKSe13/IhGBMwLSYxLyur0uMvKh5hlOdhcnouKBhRdK+Qr71sgYqmy9xYZWs6PD1TerokHRmAmqaHo7BEW4Gfw9M4QVA+TWhWY2kuJxRBU3RebXR4kJtBR0pxhpBNV1yWt8YeEgpGX4hJZZRdjNlGTlFYg8k1OUE9QUNNbaE8SWArHgA3PUcTAABSeLY8SmE0Nzw5Q1Q7dnsOAAAP9ElEQVR4nO1ba3eiOhRFnhJegogVRUSs1md91fZ2nPb//6t7ThIUrXY66962M2tlfyiQAM3mnJxXoiQJCAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICPzlICdXepqm5jeN5D/DBVA65HCmw4lepqhHhixnfydFkniAuQ5nOzxD2ekdOFmU+eiRKht/KUMpXWiyMXFBljNVltUIzszMYCcHIEPtj2FIbNsmv76tgBsbspY7jKqsteDMbcuygVI1AQ4yZQxreKl/2sA/CD8MngfPQeh/lKSdgOiMKQF1lRGmpA9VytSc9vJ2exHD3GQMI7hsdZxPHf+v4FvLbUOpKo3t0vc/+IwDslNnLlVSUNOObvZASWPXiVVDA6h5QpChXDdQyF4v/VQK76N516hWGJRGv/kxMSI1bZGiktZhSmaOA0qqJW4EMjXqsiEbueMiQ1lTVeDoxe6vX/pJCG8oP0VR8FDthh+iSKbgCTyyAyq9XJbbztxDxm4dOHXuUypQBxkai2EH52r92xiOusisur55vFkjVWXb/NBzaQ6ii8DgeHOks4E/Rmx2gGeWTKcJmp8aMmw7upsCb3X+TdbGWlWR1aBpWVbzeQtsq4/hRx50J2hZUElRfMYELWlCpyWopYqH9n3hD50WTNro6xiSIDic2w8otseRza5GK6CoPNuHbj94+zx/y5TaGKSAfgKkhEoao21pMyxq1JaiS/lahrbf71vFXLNulIrSHR06R3i9L4RoDZY/rwq0BmrKzSj4ejybuTqdjT8cM3VMV6eWpo6xnPyVWmo/g2NoFCGy1QAZllw9CbGB9/rLqlLdX6PoTigvsCB6h4rTS2xi4uxcjOdxO0upPwRljeO2Bocvi21CnGvKjUUv7NcqnJc5WI9KpXpLdZNI1LjeXlFUsvGYkgJZJEhDHH0O7g8nouxlpl54C6Q//jIRvlCnsGWs/CUo5V2ZQnALnFfU79vP1LZ2r9lWp60ahtfR0ZLg2Qz9gTuvU5evos5GnqHmeGmo8ZeJEGWEtoXJ0AfLojwhQ0JsgrppD6rH3gYNA17sy6/SowyAI9eHeLaj9+lOlC0WrUkCgdwcWofD1mLR231d/D2io1b4qJFh9Sf4ifAF4tKXEHzGQDkw5F9jZV15l4sxNj3T8Yx/CKKbDtgZmzfreOn+RlD/HxHcMSXlmhf0gc/y7mbNY5r1vk9bWHRKnunNjQ/5x/8G13H+p5inuT2xHgRnJY/XKofYTRnYF+/+fdC0/wP3uXGe/z8zlUtlzUVoj+4ql9DnEUBwVy2ZpRPY5hFXOejDXq/3AU+vdzxN84a/Z21hjlwQe9BnWcQtnVr+y/YgPUUpiVLZPrAbHljT6M2L7KR1xJuhYRJMDWvsGV7v17JhhYJ3sg/97Xd041Zr8vaJ4CdjqPRBiuFdpeDU2O4h8t5vGwXFCr3hll+9lSFkvloBLzr7R/oQYjbqJyGIMz7A0E7qqlq3r9hs/ALwwtnpfzEzVV1ceHXIpQahaPORnyLDlfTPP/9Iywa/xvi72ezzGy5oKcvtDQpgiAU3QnDWURMKGYbRckjBUC8mI97Aj7QoR5/AR3QSjVmLW5q5rJuwKF+d8NoeL+lBSHVSAwrCkNpH4hcU948sLWwwl6A01g2FucoGSxRvVlzejQcctm2FVim6owx7DHN9GkXRPO1MJpHuSsShBY174E0Z1qLJZIzDJnBXTNgxAg9sStAzi8BzStiigy/dYUuHfQfTjmbwxp1JajNIzWY1F/V/F8MdY8kFhuU6nn+7Xa+oJEizyynSA4Rvo6OyogDvRiETrlJI0EZTGjx01zfHAJYyrBeWBoRmeFnuGYYqd1yzjWmw3K4PzRip0tCnvtGJC+GOp0t4VCGINXsG9Biq1zIliIG8VB/mHrRAlBfB0M2JxroXEmYukLLIIMAWu8ObpLFamgD2KwwX9I5RfKweCFVumwQMzp5ZGfjbfQBRh0/HGyDnpxKUQLLVo7oyhimFzkJvTWPZ1C6V6ZnmdZAhu5C1OiGYZVGGWPCQzB4WPHC8MMMw+Ur1MWQmhsGiWHcC3Sp2TyRW7dI8yVnAJwOCYHjN2POOlgZzJBhsnwUnxfyC6ffMAtBQWnbX63V39cJKGP7DweQ8srpNkyr3wVFyLdXoNJy4LLkw2m0YndG7r58whHZsAFN5ylBCOUedKKtDjE8ZQkImtyY9zERyB+sh2N2rJ0nBkNDkbDyOW7lDNrPZ0YgzhpXKK3PdFreRlefClRM/DJvN0C8IBJyismSes8lrOWcMKVTO0Iju7yFR1BYOXmotbktlY3hfw/oxy5SPDBO4KZ9LtXsHjChjSDbk/v7eQTYJga+SzxPoBuFDoob1Z30IDFt4k0mN0tGB2APGsBGwEYZLKpFbHyvB0jnQavuvLCRlntBiblQ501LZo2AMtbwGoTYeHV46tSlDrZVKbmQg5TMtRVmpcrsVOYUMXTvOwL/ChTd1MMFW5XordiTG0LTtxJDpM9nwvP5qMcVUtiMqJpr3KliPCZ+f/FOOtv80AG0OqSWlISmxXvkH8s8sTUIhSUxoDsgAGaYnMkRzoI/VEkNaHdcSneVZoHyZw+fhEKal6nlYfJy6mzbvhge5DPFT0UaeqpVRqNl69dD0fSqSNcy5cF+tNgZlivZzowrWBZ5YUy31/ebLks/K12N8yhi6OgUpKJ0wBMKnDB0TmKkb18UKD6iha0a9RZvSIciwRqU6iaI2bXKdca9Fu+cmMqScHCnO6DPGm3CmWfhBZbsKMaBW7nwWxCnrskOnIUEVkgtMheEzjPrbIgbol7IoxnDOMHXPGIJBkNvgvs5kiIoHU2+I+ocyjGv3P36Aq1PHOmU4NWiR5wdlqG9mKXTDG9TYwfJz6wfEFNH4HhpbIMXd+fSy7cI8ckfXGBUWqFFekmEKjEIcrUteET1nOddn81Cl8FrpKUOSIAXZi5wzLZ2oRQkc5mHa8owFm3QJk6GEj82iBdaap2nmqTnr3rhDWkmHxrYnL1oL9I5vF0KC16Nfp0bE/wVDf3n6QEDeMGTQsjOGzNWBPGqnDG3SpsUrA/lIU5hvGp1oE5PNQzOjHlKlMkzUohtegH4QuiadwzOXMhawNqUh06IoZ0guMiRSKTJQqsuTNRu2RMoBMmSLo2QDxxwmoDmRPRXOZnBNGeJd0J+0QOT1aAGXiRQvDA8u87FJJANaUnhM8zxj0oOLjR4vNNqN8Q0hGdzrZWSSq3BUW/OLeYhvL7cHknTyvcuQ2RqmqevVy1kpg9SOAAr0L2tF9SFuutuQlLi8veiHrHK6S10HLiF2dtJkszMhJpLsFFroY9MphIHYTWj31E0pF2I606lrwg3ObrNLr61HEr/5sFqzAK37a4bhnoVy68dB07+a2VyDfcHT0kGUmwkhZxWck4azi/dfXPxfP3zAwJoVm95n6NMS/+MgtH6b3vfCxyyYlURPGDKaZYZoamjgcxU2OEP2nAMh+JtubPyGr0PLbaycVmIYNKUmOvQSQyzEVZT+9TIUTLb5cEPrC24OWfh5v4ONyddTpK78nGHw1FAaWFMry5AyvLvGEPKbNph2Q25tTALhCIT+Z2TSOlj25OtKpQWoYzyfhyE1mqCpb+bhzysMsXzP/CEGiRiQXWCIfu+rGQZhSLV0f2JLgyf0fVWQV4kh7QVhh8GFQeobzHhBhnSRfpgyhrrDKrvsyBiaTmp+Wc07CK3bbuVYMj0ypEGocsqQhq9w97b/liRdRpPVbLgZL1Q1NpkM9Q7kPjHkcWN6RIbyrpfnrcj8Eoq+dbtvVAuXj9rzPsOmUsQzle5dcGpSddxzoY5THZx6DxI8xtCNPU3NTIkeeyZlWMeVKC+XvsDgNFeNcvkebeS7DPkSB49qGncnQY0J4T3mtghMtQuGBo1D+ZEyxFIM/Mk/fz8NzxAPwMWZQ+R9iSFbtDig+lo2OWwnxjE4fIfhJMJF8M9fIbWW1aNA6Igh8b3O0IJUuFxTxNvKVhEti1oa9FWGRpS697gT5bN38B1yJ6XauBnQuG07An/Akn3pyDCkqf2jL9G6qnLz/LiuFoXTUoKIyazKKwnkPYYyuCJat1l87s42W+K1s8bNU9MKXqgQIcm3YPgKOPrgVuEMgyf4CGuf8JaXwGoOeBW8nAPj9guNzS2igy8oMURLMzsy1O0vYciXK5Ql0JOKxV1QO2LdLbFmSiTKB3PG4GHZ9wmhK9xsE4NtjdjjpToGLVQYPfB0jpT3UpszxA00+b2JG1GOWqp/gZaGrF6qPHIh+HSOKesRhGssL6IbS9hyNu4SIoyTcstKOHbAVeD1YPOdFpgPNe/NsrqmtnhMQ3lri0lOK8Pc0sw6vU+3NGxTxXEiWT/5nNyGhxFbL3fHJPe4uNFnFINB8cDhFj3Hogt1BVoR05AUy2CaQcOdM29R+0SCxVJuUe48VvWV7XEDGAkObAP/sHJaiJ0XXEtL+oS0PIPWlNT2HGRoaB4kU3MZyytqblCPLxtaHfeXgsf/3BSDBGzRge0DGpVWZpTGU/NNVS58bZR8fZeteNP1nOq+XFB05lkuq20Iz3TJhTBtAY160svbi3i6aC1i14TGbJflbMfwpyK4w9yILSBaXb4syB35/iU82TEUvtwUjoXLmZXiRjeH0wK6mdZqKdtEYUKsTd9vptDCI3DcdsIaPpcfjtt/5rsMrTWv73YDdqZU9j+boR8EdhD4YfNpz5gp64DLWtkywYUvDx/bXPtN4Lro84Xd6mPTDgtpKo3uqv/z9elu1S1C1+rWspu8YFrlwcz7FaA/Bda+cIw4I/uFrioFCv1cgiMpdipUB38FNQ6f2cTuP+wKV38r51CULnMcxK4wG3zpTVSubF6SUlHw+z8GK1co3HHY4WBfOSEJF90Bn2+0jHHYqXmGHRZydxJJkmSzmW42u2SH/KbfTpGlE3x/pYQcgz7OPo5Gt28fwoCQrc1cVFJ3MXQldzJ34/FmFi/i2Xw4A5eQTb/dGPHl4PUxiCZ+aD3f9ler1fL22Sr9bIZvL7q8d9/Nsh1hDF29ltV0Fxlmu2//+c9hN95pCc0OfMRpNSZkv1O4XDDVs6SlM4Y6ZPz4q6DYzKZ/AEGJLQAXW0jfQ5OG243LW4T1zBn2aqcMs+z7fhdTAsuLzhbLLoInw5c/hZ655gxm35HhPN90et/7Ay4OECLNcX95IyTBYHquVHSBIXF62amWmvHsj/i1ofX6uPzQz/D8wePyWiCjo0a6C2AYFQxnuuRMvvCXMe/A/uhv8ODGq18ikZjXT+CvTXMjbNF3/8cA/wwcZEvKF39ATCMgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIPBn4F9lCHjNRXwSCgAAAABJRU5ErkJggg==" />
        
      <div className="card-text">Hacktoberfest Meetup</div>
      <br />
      
      <div className="like-text">
      
      </div>
      <button className = "sidebar_button">Know More</button>
      

    </div>
    );

  }
}
 
 const domContainer = document.querySelector('#sidebar_ads');
 ReactDOM.render(<Ads />, domContainer);

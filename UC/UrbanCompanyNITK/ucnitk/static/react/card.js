'use strict';

const e = React.createElement;

class Card extends React.Component {
  constructor(props) {
    super(props);
    this.state = { liked: false };
    
  }

  render() {
    // if (this.state.liked) {
    //   return 'You liked this.';
    // }
    return (
    <div className="card" data-aos = "fade-up" data-aos-delay="100">
      <div className="card-header">
        <div className="card-title-group">
          <h5 className="card-title">Suggested For you</h5>
          
        </div>
      </div>
      
      <img className="card-image"  src = "data:image/jpeg;base64,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" alt="Logo" />
        
      
      <div className="card-text">Casuals Laundry</div>
      <br />
      
      <div className="like-text">
      
      </div>
      <button className = "sidebar_button">Order Now</button>
      

    </div>
    );
    // return (
    //   <button onClick={() => this.setState({ liked: true })}>
    //   Like
    // </button>
    // );
  }
}
 
 const domContainer = document.querySelector('#sidebar_offers');
 ReactDOM.render(<Card />, domContainer);

//  document.querySelectorAll('.sidebar_offers')
//   .forEach(domContainer => {
//     // Read the comment ID from a data-* attribute.
//     const imgSrc = parseInt(domContainer.dataset.imgSrc, 10);
//     ReactDOM.render(
//       e(LikeButton, { imgSrc: imgSrc }),
//       domContainer
//     );
//   });
import React from 'react'
import ReactPlayer from 'react-player';
import RaisedButton from 'material-ui/RaisedButton';

const styles={
  raisedButton: {
    whiteSpace: "normal",
    width: "240px",
  }
}
export default function VideoPlayBack(props) {
  console.log();
  return (<div className="row video-playback">
    <div className="video-box col-md-12">
      {props.url && 
        (<ReactPlayer
          url={props.url}
          className='react-player'
          playing
          width='500px'
          height='250px'
          controls={true}
        />)
      }
    </div>
    <div className="col-md-12">
      <RaisedButton
        label="Adjust Audio and Video Settings"
        className="btnn-video-buttons btn-vpb"
        style={styles.raisedButton}
        primary={true}
      />
    </div>

    {props.currentQuestion < 4 &&
    <div className="col-md-12">
      <RaisedButton
        label="Next Practice Question"
        className="btnn-video-buttons btn-vpb"
        style={styles.raisedButton}
        primary={true}
        onClick={() => { props.onNext() } }
      />
    </div> }

    { props.currentQuestion === 4 &&
    <div className="col-md-12">
      <RaisedButton
        label="Let's Go Live!"
        className="btnn-video-buttons btn-vpb"
        style={styles.raisedButton}
        primary={true}
      />
    </div> }

    <div className="col-md-12">
      <RaisedButton
        label="I’m Not Ready. Take Me Back to My Cruise Staff Audition Videos"
        className="btnn-video-buttons btnn-not-ready"
        style={styles.raisedButton}
        onClick={() => {props.onBack()}}
        primary={true}
      />
    </div>
  </div>)
}
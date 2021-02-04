import React, { Component } from "react";


export default class HomePage extends Component {
    constructor(props) {
      super(props);
      this.state = {
        roomCode: null,
      };
      this.clearRoomCode = this.clearRoomCode.bind(this);
    }
  
    async componentDidMount() {
      fetch("")
        .then((response) => response.json())
        .then((data) => {
          this.setState({
            roomCode: data.code,
          });
        });
    }

    render() {
        return (
          <Router>
            <Switch>
              <Route
                exact
                path="/"
                render={() => {
                  return this.state.roomCode ? (
                    <Redirect to={`/room/${this.state.roomCode}`} />
                  ) : (
                    this.renderHomePage()
                  );
                }}
              />
              <Route path="/join" component={RoomJoinPage} />
              <Route path="/info" component={Info} />
              <Route path="/create" component={CreateRoomPage} />
              <Route
                path="/room/:roomCode"
                render={(props) => {
                  return <Room {...props} leaveRoomCallback={this.clearRoomCode} />;
                }}
              />
            </Switch>
          </Router>
        );
      }
    }
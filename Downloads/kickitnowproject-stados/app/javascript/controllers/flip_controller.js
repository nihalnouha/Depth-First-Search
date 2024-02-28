import { Controller } from "@hotwired/stimulus"
// Connects to data-controller="flip"
export default class extends Controller {
  static targets = ["front","back"]
  connect() {
    console.log("connected");
  }
  flip(event){
    event.preventDefault()
    console.log("connected");
    this.frontTarget.classList.toggle("turnfront")
    this.backTarget.classList.toggle("turnback")
  }
}

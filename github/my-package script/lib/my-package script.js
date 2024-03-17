'use babel';

import MyPackage scriptView from './my-package script-view';
import { CompositeDisposable } from 'atom';

export default {

  myPackage scriptView: null,
  modalPanel: null,
  subscriptions: null,

  activate(state) {
    this.myPackage scriptView = new MyPackage scriptView(state.myPackage scriptViewState);
    this.modalPanel = atom.workspace.addModalPanel({
      item: this.myPackage scriptView.getElement(),
      visible: false
    });

    // Events subscribed to in atom's system can be easily cleaned up with a CompositeDisposable
    this.subscriptions = new CompositeDisposable();

    // Register command that toggles this view
    this.subscriptions.add(atom.commands.add('atom-workspace', {
      'my-package script:toggle': () => this.toggle()
    }));
  },

  deactivate() {
    this.modalPanel.destroy();
    this.subscriptions.dispose();
    this.myPackage scriptView.destroy();
  },

  serialize() {
    return {
      myPackage scriptViewState: this.myPackage scriptView.serialize()
    };
  },

  toggle() {
    console.log('MyPackage script was toggled!');
    return (
      this.modalPanel.isVisible() ?
      this.modalPanel.hide() :
      this.modalPanel.show()
    );
  }

};

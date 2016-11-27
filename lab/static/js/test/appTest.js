import { App } from './static/js/lib/app';

describe('App module', () => {

    let app = null;
    let mockWindow = {};

    beforeEach('setup', () => {

        mockWindow = {
            document: {
                addEventListener: jasmine.spy()
            }
        }

        app = new App(mockWindow);
    });

    it('attaches a listener for DOMContentLoaded', () => {
    });
});